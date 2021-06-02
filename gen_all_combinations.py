from generate_bingo import generate

from objectives import objectives

Nexpert = sum(1 for item in objectives if ("level" in item and item["level"] == "expert"))
Nhard = sum(1 for item in objectives if ("level" in item and item["level"] == "hard"))
Nmedium = sum(1 for item in objectives if ("level" in item and item["level"] == "medium"))
Neasy = sum(1 for item in objectives if ("level" in item and item["level"] == "easy"))

print("testing")
generate(objectives, "hard", True)
