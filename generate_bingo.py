def generate(objectives, difflevels, thisdiff, bpredrang):
    if bpredrang:
        suff = "predrang"
    else:
        suff = "all"

    # first filter (by difficulty level)
    f1obj = [item for item in objectives if difflevels[item["level"]] <= difflevels[thisdiff]]
    if bpredrang:
        # sub-filter by predrangleic
        f1obj_props = [item for item in f1obj if "props" in item.keys()]
        f1obj = [item for item in f1obj_props if "predrangleic" in item["props"]]
    # open file location
    fol = "./bingolists/"
    fname = thisdiff + "_" + suff + ".txt"  # make filename
    fpath = fol + fname
    f = open(fpath, "w")

    # main file print loop
    for i, item in enumerate(f1obj):
        if i == 0:
            f.write('[{"name" : "' + item["name"] + '"}')
        else:
            linestr = ',\n{"name" : "' + item["name"] + '"}'
            f.write(linestr)
    # fix end of file format
    f.write("\n]\n")
    f.close()
