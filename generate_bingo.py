def generate(objectives, diff, bpredrang):
    if bpredrang:
        suff = "early"
    else:
        suff = "all"

    # filter dictionary for the chosen specs
    difflevels = {"easy":   0,
                  "medium": 1,
                  "hard":   2,
                  "expert": 3
                  }

    # first filter (by difficulty level)
    f1obj = [item for item in objectives if difflevels[item["level"]] <= difflevels[diff]]

    # open file location
    fol = "./bingolists/"
    fname = diff + "_" + suff + ".txt"  # make filename
    fpath = fol + fname
    f = open(fpath, "w")

    # main file print loop
    for i, item in enumerate(f1obj):
        if i == 0:
            f.write('[{"name" : ' + item["name"] + '"}')
        else:
            linestr = ',\n{"name" : "' + item["name"] + '"}'
            f.write(linestr)
    # fix end of file format
    f.write("\n]\n")
    f.close()
