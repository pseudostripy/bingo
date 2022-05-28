from objective_definitions import *
from Objective import *
from enum import IntEnum


class LVL(IntEnum):
    TRIVIAL = 0,
    EASY = 1,
    MEDIUM = 2,
    HARD = 3,
    EXPERT = 4,
    TORTURE = 5


# Main bingo lists generation:
def generate_all():
    objs = create_objectives(objs_defn)

    # Granular control over list creation:
    # excl argument for generalise_list should be a list of string exclusions, e.g.
    # ["0*", "4R", "12K"], aka:
    #   remove trivial: all types
    #   remove expert: restriction types"
    #   remove easy,medium: kill types"

    # Easy_all
    test = generate_list("easy_all.txt",    objs, LVL.EASY,     predrang=True, excl=["0*"])
    test = generate_list("expert_all.txt",  objs, LVL.EXPERT,   predrang=True, excl=["0123O"])

    [print(vars(t)) for t in test]
    print(len(test))


def generate_list(fname, allobjs, lvl, predrang=False, excl=None):
    if excl is None:
        excl = []

    objlist = filter_objectives(allobjs, lvl, predrang, excl)
    write_file(fname, objlist)
    return objlist


def parse_exclusions(exclstr):
    # Difficulty levels
    strlvls = re.findall(r"\d", exclstr)
    lvls = [int(strlvl) for strlvl in strlvls]

    if re.match(r"\d+\*", exclstr):
        return lvls, "*"

    # Specific Task-type
    m = re.search(r"[ROTKC]", exclstr)
    if not m:
        raise ValueError("Cannot parse category type, please use '*' for all categories if you wish.")

    task_type = Objective.task_types[m[0]]
    return lvls, task_type


def exclude_set(olist, exclstr):
    # Filter by exclusions
    (excllvls, excltype) = parse_exclusions(exclstr)

    for i in range(len(excllvls)):
        el = excllvls[i]
        if excltype == "*":
            olist = [o for o in olist if not o.has_level(el)]  # keep those without matching exclusion lvl
        else:
            olist = [o for o in olist if not (o.has_level(el) and o.is_otype(excltype))]

    return olist  # filtered objective list


def filter_objectives(allobjs, lvl, predrang=False, excl=None):
    # Input parsing
    if excl is None:
        excl = []

    if isinstance(excl, str):
        excl = [excl]

    # filter by chosen difficulty level
    filt = [obj for obj in allobjs if obj.has_level(lvl)]

    # Filter by predrang
    if predrang:
        filt = [obj for obj in filt if obj.pre_drang]

    # No exclusions
    if excl == "":
        return filt

    for exclstr in excl:
        filt = exclude_set(filt, exclstr)

    return filt


def write_file(fname, objs):
    # open file location
    fol = "./bingolists/"
    fpath = fol + fname
    f = open(fpath, "w")

    # main file print loop
    for i, item in enumerate(objs):
        if i == 0:
            f.write('[{"name" : "' + item.name + '"}')
        else:
            linestr = ',\n{"name" : "' + item.name + '"}'
            f.write(linestr)
    # fix end of file format
    f.write("\n]\n")
    f.close()


# Main()
if __name__ == "__main__":
    generate_all()
