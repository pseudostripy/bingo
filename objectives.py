objectives = [
    # restriction
    {"name": "do not attune anything",          "level": "easy", "props": ["predrangleic", "restriction"]},
    {"name": "don't use a bow",                 "level": "easy", "props": ["predrangleic", "restriction"]},
    {"name": "don't speak to Lenigrast",        "level": "easy", "props": ["predrangleic", "restriction"]},
    {"name": "don't wear any armour",           "level": "easy", "props": ["predrangleic", "restriction"]},
    {"name": "don't kill any NPCs",             "level": "easy", "props": ["predrangleic", "restriction"],
     "clash": "shrodinger licia"},
    {"name": "don't use any weapon with primary thrust type", "level": "easy",
     "props": ["predrangleic", "restriction"]},
    {"name": "don't use any resins",            "level": "medium", "props": ["predrangleic", "restriction"]},
    {"name": "don't use any brightbugs",        "level": "medium", "props": ["predrangleic", "restriction"]},
    {"name": "don't use any homeward bones",    "level": "medium", "props": ["predrangleic", "restriction"]},
    {"name": "don't use the Silver Cat Ring",   "level": "medium", "props": ["predrangleic", "restriction"]},
    {"name": "don't use any small lifegems",    "level": "hard", "props": ["predrangleic", "restriction"]},
    {"name": "only heal with estus or bonfire", "level": "expert", "props": ["predrangleic", "restriction"]},
    {"name": "don't use an upgraded weapon",    "level": "expert", "props": ["predrangleic", "restriction"]},
    {"name": "only starting gear (not including rings)", "level": "expert", "props": ["predrangleic", "restriction"]},
    {"name": "don't wear damage rings", "level": "expert", "props": ["predrangleic", "restriction"]},

    # kill
    {"name": "kill the Flexile Sentry",         "level": "easy", "props": "predrangleic"},
    {"name": "kill the Rotten",                 "level": "easy", "props": "predrangleic"},
    {"name": "kill the Old Iron King",          "level": "easy", "props": "predrangleic"},
    {"name": "kill the Duke's Dear Freja",      "level": "easy", "props": "predrangleic"},
    {"name": "kill the Lost Sinner",            "level": "easy", "props": "predrangleic"},
    {"name": "kill the Executioner's Chariot",  "level": "easy", "props": "predrangleic"},
    {"name": "kill the Belfry Gargoyles",       "level": "easy", "props": "predrangleic"},
    {"name": "kill the Royal Rat Vanguard",     "level": "easy", "props": "predrangleic"},
    {"name": "kill the Royal Rat Authority",    "level": "easy", "props": "predrangleic"},
    {"name": "kill the Old Dragonslayer",       "level": "easy", "props": "predrangleic"},
    {"name": "Kill Velstadt",                   "level": "easy"},
    {"name": "kill Vengarl's body",             "level": "easy", "props": "predrangleic"},
    {"name": "kill Vengarl's head",             "level": "easy", "props": "predrangleic"},
    {"name": "Kill Benhart of Jugo",            "level": "easy", "props": "predrangleic",
     "clash": "shrodinger benhart"},
    {"name": "kill Vendrick",                   "level": "hard", "props": "predrangleic"},
    {"name": "kill Ancient Dragon",             "level": "hard"},
    {"name": "kill the Gank Squad",             "level": "hard", "props": "predrangleic"},
    {"name": "kill Sinh the Slumbering Dragon", "level": "hard", "props": "predrangleic"},
    {"name": "kill Elana, Squalid Queen",       "level": "hard", "props": "predrangleic"},
    {"name": "kill Aava the King's Pet",        "level": "hard"},
    {"name": "kill the Blue Smelter Demon",     "level": "expert", "props": "predrangleic"},
    {"name": "kill the Fume Knight",            "level": "expert", "props": "predrangleic"},
    {"name": "kill Sir Alonne",                 "level": "expert"},
    {"name": "kill the Burnt Ivory King",       "level": "expert"},
    {"name": "kill Lud and Zallen",             "level": "expert"},
    {"name": "kill Darklurker",                 "level": "expert"},
    {"name": "kill Aldia",                      "level": "expert"},
    {"name": "kill Mauldron the Assassin",      "level": "expert", "props": "predrangleic"},

    # kill challenges
    {"name": "kill the Pursuer without ballista or quick kill", "level": "easy", "props": "predrangleic"},
    {"name": "kill Dragonrider with a full arena",              "level": "easy", "props": "predrangleic"},
    {"name": "kill 5 pursuers",                 "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with consumables",    "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with a bow",          "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with a crossbow",     "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss on ng+7",             "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with only pyromancy", "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with only hexes",     "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with only miracles",  "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with only sorceries", "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with a whip",         "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with a boss weapon",  "level": "medium", "props": "predrangleic"},
    {"name": "kill a lord without leveling",    "level": "medium", "props": "predrangleic"},
    {"name": "kill a lord with the dagger",     "level": "medium", "props": "predrangleic"},
    {"name": "kill a lord with the uchigatana", "level": "medium", "props": "predrangleic"},
    {"name": "kill a boss with a broken weapon", "level": "hard", "props": "predrangleic"},
    {"name": "kill a boss using only a shield", "level": "hard", "props": "predrangleic"},
    {"name": "kill a boss with only dung pies", "level": "hard", "props": "predrangleic"},
    {"name": "kill a boss dressed as havel with the dragon tooth (no greatshield)", "level": "hard",
     "props": "predrangleic"},
    {"name": "kill a boss using a fire longsword while wearing Vengarl's helm and the drangleic sheild",
     "level": "hard", "props": "predrangleic"},
    {"name": "kill a boss with the butterfly set",      "level": "hard", "props": "predrangleic"},
    {"name": "kill a boss with it's own boss weapon",   "level": "hard", "props": "predrangleic"},
    {"name": "kill a boss with fists",          "level": "hard", "props": "predrangleic"},
    {"name": "kill a lord with only sorceries", "level": "hard", "props": "predrangleic"},
    {"name": "kill a lord with only pyromancies", "level": "hard", "props": "predrangleic"},
    {"name": "kill a lord with only miracles",  "level": "hard", "props": "predrangleic"},
    {"name": "kill a lord with only hexes",     "level": "hard", "props": "predrangleic"},
    {"name": "kill a boss with torch",          "level": "expert", "props": "predrangleic"},
    {"name": "kill a boss with the ladle",      "level": "expert", "props": "predrangleic"},
    {"name": "kill a boss with a greatbow",     "level": "expert", "props": "predrangleic"},
    {"name": "Kill chariot without pulling the lever",  "level": "expert", "props": "predrangleic"},

    # obtain
    {"name": "obtain the Stone Ring",           "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Hawk Ring",            "level": "easy", "props": "predrangleic"},
    {"name": "obtain Cale's Helm",              "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Ring of Binding",      "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Knight Set",           "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Ring of Giants +0",    "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Bone Staff",           "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Archdrake Shield",     "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Hush sorcery",         "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Ring of Knowledge",    "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Forlorn Hood",         "level": "easy", "props": "predrangleic"},
    {"name": "obtain a Dragon Tooth",           "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Blue Tearstone Ring",  "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Blossom Kite Shield",  "level": "easy", "props": "predrangleic"},
    {"name": "obtain Ricard's Rapier",          "level": "easy", "props": "predrangleic"},
    {"name": "obtain Soul Spear",               "level": "easy", "props": "predrangleic"},
    {"name": "obtain the spell Chameleon",      "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Old Knight Pike",      "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Poinsonbite Ring",     "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Mirrah Shield",        "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Ash Knuckle Ring",     "level": "easy", "props": "predrangleic"},
    {"name": "obtain Havel's Armour Set",       "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Dark Pyromancy Flame", "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Heide Lance",          "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Bandit's Greataxe",    "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Shotel",               "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Old Sun Ring",         "level": "easy", "props": "predrangleic"},
    {"name": "obtain a Murakumo",               "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Santier's Spear",      "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Gyrm Axe",             "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Staff of Wisdom",      "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Pickaxe",              "level": "hard", "props": "predrangleic"},
    {"name": "obtain the Priestess Set",        "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Blacksmith's Hammer",  "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Singer's Dress",       "level": "easy"},
    {"name": "obtain the Red Iron Twinblade",   "level": "easy"},
    {"name": "obtain the Helix Halberd",        "level": "easy"},
    {"name": "obtain warmth",                   "level": "easy"},
    {"name": "obtain Immolation",               "level": "easy", "props": "predrangleic"},
    {"name": "obtain 2 darkdrift katanas",      "level": "easy"},
    {"name": "obtain both pyromancy flames",    "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Avelyn",               "level": "easy"},
    {"name": "obtain Oldenford's Staff",        "level": "easy"},
    {"name": "obtain a Dragon Acolyte Mask",    "level": "easy"},
    {"name": "obtain the Third Dragon Ring",    "level": "easy"},
    {"name": "obtain the Drangleic Helm",       "level": "easy"},
    {"name": "obtain the Giant Warrior Club",   "level": "easy"},
    {"name": "obtain the Ring of Resistance",   "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Mirrah Greatsword",    "level": "easy", "props": "predrangleic"},
    {"name": "obtain the ladle",                "level": "easy", "props": "predrangleic"},
    {"name": "obtain darkdrift",                "level": "easy"},
    {"name": "obtain the Gyrm Greataxe",        "level": "easy", "props": "predrangleic"},
    {"name": "obtain the ring of the dead",     "level": "easy"},
    {"name": "obtain the Royal Soldier's Ring +0",          "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Covetous Gold Serpent Ring +0",    "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Great Magic Weapon sorcery",       "level": "easy", "props": "predrangleic"},
    {"name": "obtain the black knight ultra greatsword",    "level": "easy", "props": "predrangleic"},
    {"name": "obtain the Northern Ritual Band +2",          "level": "easy"},
    {"name": "obtain Gower's Ring of Protection",           "level": "easy"},
    {"name": "obtain the Engraved Gauntlets",   "level": "medium", "props": "predrangleic"},
    {"name": "obtain 4 Rings of the Evil Eye",  "level": "medium", "props": "predrangleic"},
    {"name": "obtain the Sanctum Mace",         "level": "medium", "props": "predrangleic"},
    {"name": "obtain Promised Walk of Peace",   "level": "medium", "props": "predrangleic"},
    {"name": "obtain Denial",                   "level": "medium", "props": "predrangleic"},
    {"name": "obtain the Puzzling Stone Sword", "level": "medium", "props": "predrangleic"},
    {"name": "obtain the Sanctum Shield",       "level": "medium", "props": "predrangleic"},
    {"name": "obtain the Old Bell Helm",        "level": "medium"},
    {"name": "obtain the Ring of the Embedded", "level": "medium"},
    {"name": "obtain Flying Feline Boots",      "level": "medium", "props": "predrangleic"},
    {"name": "obtain Flame Weapon",             "level": "medium", "props": "predrangleic"},
    {"name": "obtain the chaos blade",          "level": "medium", "props": "predrangleic"},
    {"name": "obtain the Crypt Blacksword",     "level": "medium", "props": "predrangleic"},
    {"name": "obtain the Drakeblood Greatsword",    "level": "medium", "props": "predrangleic"},
    {"name": "obtain the Dragonslayer Greatbow",    "level": "medium", "props": "predrangleic"},
    {"name": "obtain the Moonlight Greatsword",     "level": "medium", "props": "predrangleic"},
    {"name": "obtain the curved dragon greatsword", "level": "medium"},
    {"name": "obtain the Simpleton's Ring",     "level": "hard", "props": "predrangleic"},
    {"name": "obtain the Pilgrim's Spontoon",   "level": "hard", "props": "predrangleic"},
    {"name": "obtain the Majestic Greatsword",  "level": "hard", "props": "predrangleic"},
    {"name": "obtain the Bone Fist",            "level": "hard"},
    {"name": "obtain Unleash Magic",            "level": "hard"},
    {"name": "obtain the King's Crown",         "level": "hard"},
    {"name": "obtain clear bluestone ring +0, +1, and +2",      "level": "hard", "props": "predrangleic"},
    {"name": "obtain chloranthy ring +0, +1, and +2",           "level": "hard", "props": "predrangleic"},
    {"name": "obtain life ring +0, +1, +2, and +3",             "level": "hard"},
    {"name": "obtain Spell Quartz ring +0, +1, +2, and +3",     "level": "hard"},
    {"name": "obtain Flame Quartz ring +0, +1, +2, and +3",     "level": "hard"},
    {"name": "obtain Thunder Quartz ring +0, +1, +2, and +3",   "level": "hard"},
    {"name": "obtain 4 silver covertous serpent rings",         "level": "hard", "props": "predrangleic"},
    {"name": "obtain 6 covetous serpent rings (gold and silver)", "level": "hard", "props": "predrangleic"},
    {"name": "obtain Outcry",                           "level": "expert", "props": "predrangleic"},
    {"name": "obtain the Ivory Warrior Ring",           "level": "expert"},
    {"name": "obtain the Curved Nil Greatsword",        "level": "expert"},
    {"name": "obtain the Chime of Screams (Nadalia)",   "level": "expert"},
    {"name": "obtain Ring of Blades +0, +1, and +2",    "level": "expert"},
    {"name": "obtain Ring of the Living",               "level": "expert"},

    # purchases
    {"name": "purchase the Smelter Demon set",                          "level": "easy", "props": "predrangleic"},
    {"name": "purchase the Lost Sinner set",                            "level": "easy", "props": "predrangleic"},
    {"name": "purchase the Looking Glass Knight set",                   "level": "easy"},
    {"name": "purchase all 4 pieces of the Moonlight Butterfly set",    "level": "medium", "props": "predrangleic"},

    # tasks
    {"name": "join the Heirs of the Sun",       "level": "easy", "props": "predrangleic"},
    {"name": "join the Way of the Blue",        "level": "easy", "props": "predrangleic"},
    {"name": "join the Brotherhood of Blood",   "level": "easy", "props": "predrangleic"},
    {"name": "join the Blue Sentinels",         "level": "easy", "props": "predrangleic"},
    {"name": "join the Bell Keepers",           "level": "easy", "props": "predrangleic"},
    {"name": "join the Rat King covenant",      "level": "easy", "props": "predrangleic"},
    {"name": "join the Company of Champions",   "level": "easy", "props": "predrangleic"},
    {"name": "join the Pilgrims of Dark",       "level": "easy"},
    {"name": "join the Dragon Remnants covenant", "level": "easy"},
    {"name": "use Gillian to place any ladder", "level": "easy", "props": "predrangleic"},
    {"name": "infuse a weapon",                 "level": "easy", "props": "predrangleic"},
    {"name": "get 7 estus flask uses",          "level": "easy", "props": "predrangleic"},
    {"name": "upgrade the estus flask to +4",   "level": "easy", "props": "predrangleic"},
    {"name": "spice a spell at Magerold",       "level": "easy", "props": "predrangleic"},
    {"name": "level a stat to 99",              "level": "easy", "props": "predrangleic"},
    {"name": "upgrade a weapon to +10",         "level": "easy", "props": "predrangleic"},
    {"name": "kill 3 invisible hollows",        "level": "easy", "props": "predrangleic"},
    {"name": "change the nature of your being", "level": "easy", "props": "predrangleic"},
    {"name": "start as deprived",               "level": "easy", "props": "predrangleic", "clash": "starting_class"},
    {"name": "start as cleric",                 "level": "easy", "props": "predrangleic", "clash": "starting_class"},
    {"name": "start as sorcerer",               "level": "easy", "props": "predrangleic", "clash": "starting_class"},
    {"name": "start without a gift",            "level": "easy", "props": "predrangleic", "clash": "starting_gift"},
    {"name": "start deprived with no gift",     "level": "easy", "props": "predrangleic",
     "clash": ["starting_class", "starting_gift"]},
    {"name": "light all 5 bonfires in The Lost Bastile",            "level": "easy", "props": "predrangleic"},
    {"name": "light all 4 bonfires in Drangleic Castle",            "level": "easy"},
    {"name": "light all 4 bonfires in Shrine of Amana",             "level": "easy"},
    {"name": "light all 4 bonfires in Forest of Fallen Giants",     "level": "easy", "props": "predrangleic"},
    {"name": "ring the bells of both belfries",                     "level": "easy", "props": "predrangleic"},
    {"name": "get unpoisoned by the gutter bug",                    "level": "easy", "props": "predrangleic"},
    {"name": "trade one boss soul with each vendor",                "level": "easy", "props": "predrangleic"},
    {"name": "do 5 trades with Dyna and Tillo",                     "level": "easy", "props": "predrangleic"},
    {"name": "reverse hollowing at the amana shrine",               "level": "medium"},
    {"name": "attune one of each type of spell at the same time",   "level": "medium", "props": "predrangleic"},
    {"name": "traverse 2 fog walls from behind",                    "level": "medium", "props": "predrangleic"},
    {"name": "repair a weapon at the whipping tree",                "level": "medium", "props": "predrangleic"},
    {"name": "talk to Gavlan in all 3 locations",                   "level": "medium", "props": "predrangleic"},
    {"name": "have at least one of each arrow type in your inventory",          "level": "medium"},
    {"name": "have at least one of each great arrow type in your inventory",    "level": "medium"},
    {"name": "have at least one of each bolt type in your inventory",           "level": "medium"},
    {"name": "activate the dragon in Aldia's Keep",                 "level": "hard"},
    {"name": "cut off things from 3 different bosses",              "level": "hard", "props": "predrangleic"},
    {"name": "enter the fume knight fight wearing velstadts helm",  "level": "hard"},
    {"name": "upgrade a weapon with twinkling titanite to +5",      "level": "hard", "props": "predrangleic"},
    {"name": "upgrade a weapon with petrified dragon bones to +5",  "level": "hard", "props": "predrangleic"},
    {"name": "invade and kill licia",               "level": "expert"},
    {"name": "get all gestures",                    "level": "expert"},
    {"name": "Parry 5 bosses",                      "level": "expert", "props": "predrangleic"},
    {"name": "join all covenants",                  "level": "expert"},
    {"name": "light all 5 bonfires in Brume Tower", "level": "expert", "props": "predrangleic"},
    {"name": "light all 5 bonfires in Eleum Loyce", "level": "expert"},
    {"name": "inherit Benhart's armour",            "level": "expert", "clash": "shrodinger Benhart"},
    {"name": "inherit Lucatiel's armour",           "level": "expert", "clash": "shrodinger Lucatiel"},
    {"name": "kill Gutter Denizen (gutter sconses)",                "level": "expert", "props": "predrangleic"},
    {"name": "kill Greatsword Foreigner phantom (Things Betwitx)",  "level": "expert", "props": "predrangleic"},
    {"name": "return a strong heat to the crowns (4 crowns)",       "level": "expert"},
    {"name": "have all available NPCs alive in Majula together (gathering of exiles)", "level": "expert",
     "props": "predrangleic"},
]

