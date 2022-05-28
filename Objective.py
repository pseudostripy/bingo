import re
from enum import Enum, auto


class TaskType(Enum):
    RESTRICTION = auto()
    OBTAIN = auto()
    TASK = auto()
    KILL = auto()
    KILLCHALLENGE = auto()


class Objective:
    """Define bingo objective and parse properties for later filtering"""

    def __init__(self, input1, input2=''):
        # constructor when passed (name, props)
        if isinstance(input1, str):
            self.name = input1
            propstr = input2

        # constructor when passed [name,props]
        elif isinstance(input1, list):
            self.name = input1[0]
            propstr = input1[1]

        else:
            # Unexpected constructor argument call
            raise TypeError()

        # Parse properties
        (self.levels, self.task_type, self.pre_drang) = self.parse_properties(propstr)
        self.minlvl = min(self.levels)

    # Static dictionary:
    task_types = {'R': TaskType.RESTRICTION,
                  'O': TaskType.OBTAIN,
                  'T': TaskType.TASK,
                  'K': TaskType.KILL,
                  'C': TaskType.KILLCHALLENGE}

    def parse_properties(self, propstr):
        # Difficulty levels
        strlvls = re.findall(r"\d", propstr)
        lvls = [int(strlvl) for strlvl in strlvls]

        # check for level+ (shorthand call)
        if len(lvls) == 1:
            if re.match(r"\d\+", propstr):
                [lvls.append(i) for i in range(lvls[0] + 1, 7)]  # 7 = torture

        # Task-type
        m = re.search(r"[ROTKC]", propstr)
        task_type = self.task_types[m[0]]

        # Pre-drang check
        m = re.search(r"P", propstr)
        predrang = True if m else False

        return lvls, task_type, predrang

    def has_level(self, lvl):
        return lvl in self.levels

    def is_otype(self, typ):
        return self.task_type == typ


def create_objectives(objlist):
    if not objlist:
        return None

    nrows = len(objlist)
    return [Objective(objlist[i]) for i in range(nrows)]
