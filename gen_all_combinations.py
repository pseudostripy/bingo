from generate_bingo import generate
from objectives import objectives

# filter dictionary for the chosen specs
difflevels = {"easy":   0,
              "medium": 1,
              "hard":   2,
              "expert": 3,
              "torture": 4
              }

for key in difflevels.keys():
    generate(objectives, difflevels, key, True)   # pre-drangleic tasks only
    generate(objectives, difflevels, key, False)  # any tasks

