from objective_definitions import *
from Objective import *
from enum import IntEnum
import os

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

    stdfol = "./bingolists/standard"
    miscfol = "./bingolists/misc"

    # Standard boards:
    generate_list(stdfol, "easy_predrang.txt",      objs, LVL.EASY,     predrang=True)
    generate_list(stdfol, "med_predrang.txt",       objs, LVL.MEDIUM,   predrang=True)
    generate_list(stdfol, "hard_predrang.txt",      objs, LVL.HARD,     predrang=True)
    generate_list(stdfol, "expert_predrang.txt",   objs, LVL.EXPERT,   predrang=True)
    generate_list(stdfol, "easy_all.txt",           objs, LVL.EASY)
    generate_list(stdfol, "med_all.txt",            objs, LVL.MEDIUM)
    generate_list(stdfol, "hard_all.txt",           objs, LVL.HARD)
    generate_list(stdfol, "expert_all.txt",         objs, LVL.EXPERT)

    # Misc. boards:
    generate_list(miscfol, "hard_minmed_pre.txt",     objs, LVL.EXPERT, predrang=True,  excl="01*")
    generate_list(miscfol, "hard_minmed_all.txt",     objs, LVL.EXPERT, predrang=False, excl="01*")
    generate_list(miscfol, "expert_minhard_pre.txt",  objs, LVL.EXPERT, predrang=True,  excl="012*")
    generate_list(miscfol, "expert_minhard_all.txt",  objs, LVL.EXPERT, predrang=False, excl="012*")
    generate_list(miscfol, "med_norestrict_pre.txt",  objs, LVL.MEDIUM, predrang=True,  excl="012R")
    generate_list(miscfol, "med_norestrict_all.txt",  objs, LVL.MEDIUM, predrang=False, excl="012R")
    generate_list(miscfol, "hard_norestrict_pre.txt", objs, LVL.HARD,   predrang=True,  excl="0123R")
    generate_list(miscfol, "hard_norestrict_all.txt", objs, LVL.HARD,   predrang=False, excl="0123R")
    generate_list(miscfol, "hard_killchallenges_pre.txt", objs, LVL.HARD, predrang=True,
                  excl=["0123R", "0123O", "0123T", "0123K"])
    generate_list(miscfol, "hard_killchallenges_all.txt", objs, LVL.HARD, predrang=False,
                  excl=["0123R", "0123O", "0123T", "0123K"])
    generate_list(miscfol, "expert_killchallenges_pre.txt", objs, LVL.EXPERT, predrang=True,
                  excl=["01234R", "01234O", "01234T", "01234K"])
    generate_list(miscfol, "hard_killchallenges_all.txt", objs, LVL.EXPERT, predrang=False,
                  excl=["01234R", "01234O", "01234T", "01234K"])


def generate_list(fol, fname, allobjs, lvl, predrang=False, excl=None):
    if excl is None:
        excl = []

    objlist = filter_objectives(allobjs, lvl, predrang, excl)

    if not os.path.isdir(fol):
        os.mkdir(fol)

    fpath = fol + "/" + fname
    write_file(fpath, objlist)
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


def write_file(fpath, objs):
    # open file location
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
    print("Run complete!")
