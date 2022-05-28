class Objective:
    """Define bingo objective and properties for filtering"""

    def __init__(self, name, propstr=''):
        # constructor when passed (name, props)
        if isinstance(name, str):
            self.name = name
            self.parse_properties(propstr)
            return
        # constructor when passed [name,props]
        elif isinstance(name, list):
            inputlist = name
            self.name = inputlist[0]
            self.parse_properties(inputlist[1])

    def parse_properties(self, propstr):
        return


def create_objectives(objlist):
    if not objlist:
        return None

    nrows = len(objlist)
    return [Objective(objlist[i]) for i in range(nrows)]
