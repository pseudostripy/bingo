from generate_bingo import generate
from objectives import objectives

# filter dictionary for the chosen specs
catinfo = [{"name": "trivial",  "difficulty": 0, "mindifficulty": 0},
           {"name": "easy",     "difficulty": 1, "mindifficulty": 0},
           {"name": "medium",   "difficulty": 2, "mindifficulty": 0},
           {"name": "hard",     "difficulty": 3, "mindifficulty": 0},
           {"name": "expert",   "difficulty": 4, "mindifficulty": 0},
           {"name": "torture",  "difficulty": 5, "mindifficulty": 1},
           ]

# Generate these types:
genboards = ["easy", "medium", "hard", "expert", "torture"]

for board in genboards:
    generate(objectives, catinfo, board, True)   # pre-drangleic tasks only
    generate(objectives, catinfo, board, False)  # any tasks
