
# Property descriptor examples:
# Level-type
#   0+ = (shorthand) Relevant for trivial (0) through torture (5)
#   3  = Only relevant for Hard (3)
#   12 = Relevant for easy (1), and medium (2) only.
# Task-type
#   R = Restriction objective
#   O = Obtain objective
#   T = Task objective
#   K = Kill objective
#   C = kill Challenge objective
# Other classifiers:
#   P = Pre-drangleic

objs_defn = [
    # restriction
    ["do not attune anything",          "1+ R P"],

    ["don't shoot from a bow",          "012 R P"],  # trivial-medium version
    ["don't use a bow",                 "3 R P"],    # hard-specific version
    ["don't use a bow or crossbow",     "4+ R P"],   # expert+ version

    ["don't speak to Lenigrast",        "1+ P R"],
    ["don't wear any armour",           "1+ P R"],
    ["don't kill any NPCs",             "1+ P R"],
    ["don't use any weapon with primary thrust type", "1+ P R"],
    ["don't use any resins",            "2+ R P"],
    ["don't use any brightbugs",        "2+ R P"],
    ["don't use any homeward bones",    "2+ R P"],
    ["don't use the Silver Cat Ring",   "2+ R P"],
    ["don't use any small lifegems",    "3+ R P"],
    ["don't pop any souls",             "3+ R P"],
    ["don't talk to Melentia",          "3+ R P"],
    ["only heal with estus or bonfire", "4+ R P"],
    ["don't upgrade a weapon",          "4+ R P"],
    ["only use NPC drops as weapons",   "4+ R P"],
    ["only starting gear (not including rings)", "4+ R P"],
    ["don't wear damage rings",         "4+ R P"],
    ["no levelling",                    "5+ R P"],

    # kill
    ["kill the Rotten",                 "0+ K P"],
    ["kill the Old Iron King",          "0+ K P"],
    ["kill the Duke's Dear Freja",      "0+ K P"],
    ["kill the Lost Sinner",            "0+ K P"],
    ["kill Velstadt",                   "0+ K"],
    ["kill Vengarl's head",             "0+ K P"],
    ["Kill Benhart of Jugo",            "0+ K P"],
    ["kill the Flexile Sentry",         "1+ K P"],
    ["kill the Executioner's Chariot",  "1+ K P"],
    ["kill the Belfry Gargoyles",       "1+ K P"],
    ["kill the Royal Rat Vanguard",     "1+ K P"],
    ["kill the Royal Rat Authority",    "1+ K P"],
    ["kill the Old Dragonslayer",       "1+ K P"],
    ["kill Vengarl's body",             "1+ K P"],
    ["kill Vendrick",                   "3+ K"],
    ["kill Ancient Dragon",             "3+ K"],
    ["kill the Gank Squad",             "3+ K P"],
    ["kill Sinh the Slumbering Dragon", "3+ K P"],
    ["kill Elana, Squalid Queen",       "3+ K P"],
    ["kill Aava the King's Pet",        "3+ K"],
    ["kill the Blue Smelter Demon",     "4+ K P"],
    ["kill the Fume Knight",            "4+ K P"],
    ["kill Sir Alonne",                 "4+ K"],
    ["kill the Burnt Ivory King",       "4+ K"],
    ["kill Lud and Zallen",             "4+ K"],
    ["kill Darklurker",                 "4+ K"],
    ["kill Aldia",                      "4+ K"],
    ["kill Mauldron the Assassin",      "4+ K P"],

    # kill challenges
    ["kill the Pursuer without ballista or quick kill", "1+ C P"],
    ["kill Dragonrider with a full arena",              "1+ C P"],
    ["kill a boss with powerstanced weapons",           "1+ C P"],
    ["kill a boss with an NPC dropped weapon",          "1+ C P"],
    ["kill Najka with summoning Tark",                  "1+ C P"],

    ["kill 3 Pursuers",                 				"2 C P"],   # medium-specific
    ["kill 5 Pursuers",                 				"3 C P"],   # hard-specific
    ["kill 7 Pursuers",                 				"4+ C P"],  # expert+

    ["kill a boss with consumables",    				"2+ C P"],
    ["kill a boss with a bow",          				"2+ C P"],
    ["kill a boss with a crossbow",     				"2+ C P"],
    ["kill a boss on ng+7",             				"2+ C P"],
    ["kill a boss with only pyromancy", 				"2+ C P"],
    ["kill a boss with only hexes",     				"2+ C P"],
    ["kill a boss with only miracles",  				"2+ C P"],
    ["kill a boss with only sorceries", 				"2+ C P"],
    ["kill a boss with a whip",         				"2+ C P"],
    ["kill a boss with a boss weapon",  				"2+ C P"],
    ["kill a lord without leveling",    				"2+ C P"],
    ["kill a lord with the dagger",     				"2+ C P"],
    ["kill a lord with the uchigatana", 				"2+ C P"],
    ["kill a lord whilst in Covenant of Champions", 	"2+ C P"],
    ["kill a boss with broken santiers spear", 			"2+ C P"],
    ["kill a boss with a poisonous weapon (no resin)",  "2+ C P"],
    ["kill a boss with a lightning weapon (no resin)",  "2+ C P"],
    ["kill a boss with a bleed weapon (no resin)",      "2 C P"],
    ["kill a boss with a magic weapon (no resin)",      "2 C P"],
    ["kill a boss with a fire weapon (no resin)",       "2 C P"],
    ["kill Old Dragonslayer as your first boss", 		"3+ C P"],
    ["kill Najka as your first boss", 					"3+ C P"],
    ["kill a boss with a broken weapon", 				"3+ C P"],
    ["kill a boss using only a shield", 				"3+ C P"],
    ["kill a boss with only dung pies", 				"3+ C P"],

    ["kill a dragon boss with dragonslayer spear", 		"3 C"],     # hard-all
    ["kill a dragon boss with dragonslayer spear", 		"4+ C P"],  # expert+ predrang/all

    ["kill a boss with the butterfly set",      		"3+ C P"],
    ["kill a boss with it's own boss weapon",   		"3+ C P"],
    ["kill a boss with fists",          				"3+ C P"],
    ["kill a lord with only sorceries", 				"3+ C P"],
    ["kill a lord with only pyromancies", 				"3+ C P"],
    ["kill a lord with only miracles",  				"3+ C P"],
    ["kill a lord with only hexes",     				"3+ C P"],
    ["kill a boss dressed as Havel with the dragon tooth (no greatshield)",                             "3+ C P"],
    ["kill a boss using a fire longsword while wearing Vengarl's helm and the drangleic sheild",        "3+ C P"],
    ["kill a dragonrider boss wearing dragonrider set and using dragonrider weapons and shield",        "3+ C"],
    ["kill a boss as a female wearing full mirrah (Lucatiel) set, using mirrah greatsword and shield",  "4+ K"],
    ["kill a boss with torch",          				"4+ C P"],
    ["kill a boss with the ladle",      				"4+ C P"],
    ["kill a boss with a greatbow",     				"4+ C P"],
    ["kill chariot without pulling the lever",  		"4+ C P"],
    ["kill one lord 6 times with all 6 resins", 		"4+ C P"],
    ["kill Alonne without getting hit (Sudoku)", 		"4+ C"],
    ["kill a boss with powerstanced Smelter swords (blue and red)", "5 C P"],

    # obtain
    ["obtain the Stone Ring",           "0+ O P"],
    ["obtain the Hawk Ring",            "0+ O P"],
    ["obtain Cale's Helm",              "0+ O P"],
    ["obtain the Ring of Binding",      "0+ O P"],
    ["obtain the Knight Set",           "0+ O P"],
    ["obtain the Ring of Giants +0",    "0+ O P"],
    ["obtain the Bone Staff",           "012 O P"],
    ["obtain the Archdrake Shield",     "0+ O P"],
    ["obtain the Hush sorcery",         "012 O P"],
    ["obtain the Blue Tearstone Ring",  "0+ O P"],
    ["obtain the Blossom Kite Shield",  "012 O P"],
    ["obtain Ricard's Rapier",          "0+ O P"],
    ["obtain Soul Spear",               "012 O P"],
    ["obtain the Poinsonbite Ring",     "012 O P"],
    ["obtain the Dark Pyromancy Flame", "012 O P"],
    ["obtain the Priestess Set",        "012 O P"],
    ["obtain the Blacksmith's Hammer",  "012 O P"],
    ["obtain the Forlorn Hood",         "1+ O P"],
    ["obtain a Dragon Tooth",           "1+ O P"],
    ["obtain the spell Chameleon",      "1+ O P"],
    ["obtain the Old Knight Pike",      "1+ O P"],
    ["obtain the Mirrah Shield",        "1+ O P"],
    ["obtain the Ash Knuckle Ring",     "012 O P"],
    ["obtain Havel's Armour Set",       "12 O P"],
    ["obtain the Heide Lance",          "1+ O P"],
    ["obtain the Bandit's Greataxe",    "1+ O P"],
    ["obtain the Shotel",               "012 O P"],
    ["obtain the Old Sun Ring",         "1+ O P"],
    ["obtain a Murakumo",               "1+ O P"],
    ["obtain the Santier's Spear",      "1+ O P"],
    ["obtain the Gyrm Axe",             "1+ O P"],
    ["obtain the Staff of Wisdom",      "1+ O P"],
    ["obtain Protective Chime",         "12 O P"],
    ["obtain Immolation",               "1+ O P"],
    ["obtain both pyromancy flames",    "1+ O P"],
    ["obtain the Ring of Resistance",   "12 O P"],
    ["obtain the Mirrah Greatsword",    "1+ O P"],
    ["obtain the Gyrm Greataxe",        "1+ O P"],
    ["obtain the ladle",                "1+ O P"],
    ["obtain the Royal Soldier's Ring +0",          "1+ O P"],
    ["obtain the Covetous Gold Serpent Ring +0",    "1+ O P"],
    ["obtain the Great Magic Weapon sorcery",       "12 O P"],
    ["obtain the black knight ultra greatsword",    "1+ O P"],
    ["obtain the Singer's Dress",       "1+ O"],
    ["obtain the Red Iron Twinblade",   "1+ O"],
    ["obtain the Helix Halberd",        "1+ O"],
    ["obtain warmth",                   "1+ O"],
    ["obtain 2 darkdrift katanas",      "1+ O"],
    ["obtain the Avelyn",               "1+ O"],
    ["obtain Oldenford's Staff",        "1+ O"],
    ["obtain a Dragon Acolyte Mask",    "1+ O"],
    ["obtain the Third Dragon Ring",    "1+ O"],
    ["obtain the Drangleic Helm",       "1+ O"],
    ["obtain the Giant Warrior Club",   "1+ O"],
    ["obtain darkdrift",                "1+ O"],
    ["obtain the ring of the dead",     "1+ O"],
    ["obtain the Northern Ritual Band +2",	"1+ O"],
    ["obtain Gower's Ring of Protection",   "1+ O"],
    ["obtain the Engraved Gauntlets",   "2+ O P"],
    ["obtain the Sanctum Mace",         "2 O P"],
    ["obtain Promised Walk of Peace",   "2 O P"],
    ["obtain Denial",                   "2+ O P"],
    ["obtain the Puzzling Stone Sword", "2+ O P"],
    ["obtain the Sanctum Shield",       "2+ O P"],
    ["obtain Flying Feline Boots",      "2+ O P"],
    ["obtain Flame Weapon",             "2+ O P"],
    ["obtain the chaos blade",          "2+ O P"],
    ["obtain the Crypt Blacksword",     "2+ O P"],
    ["obtain the Drakeblood Greatsword",    "2+ O P"],
    ["obtain the Dragonslayer Greatbow",    "2+ O P"],
    ["obtain the Moonlight Greatsword",     "2+ O P"],
    ["obtain the Curved Dragon Greatsword", "2+ O P"],
    ["obtain the Old Bell Helm",        "2+ O"],
    ["obtain the Ring of the Embedded", "2+ O"],
    ["obtain the (visible) Aurous set", "3+ O P"],
    ["obtain the Simpleton's Ring",     "3+ O P"],
    ["obtain the Pilgrim's Spontoon",   "3+ O P"],
    ["obtain the Majestic Greatsword",  "3+ O P"],

    ["obtain two quartz +1 rings",      "3 O P"],   # hard-specific
    ["obtain all 4 quartz +1 rings",    "4+ O P"],  # expert+

    ["obtain the Pickaxe",              "3+ O P"],
    ["obtain the Bone Fist",            "3+ O"],
    ["obtain Unleash Magic",            "3+ O"],
    ["obtain the King's Crown",         "3+ O"],
    ["obtain clear bluestone ring +0, +1, and +2",      	"3+ O P"],
    ["obtain chloranthy ring +0, +1, and +2",           	"3+ O P"],
    ["obtain 4 Silver Covetous Serpent rings",         		"3+ O P"],
    ["obtain 6 Covetous Serpent rings (gold and silver)",   "3+ O P"],
    ["obtain life ring +0, +1, +2, and +3",             "3+ O"],
    ["obtain Spell Quartz ring +0, +1, +2, and +3",     "3+ O"],
    ["obtain Flame Quartz ring +0, +1, +2, and +3",     "3+ O"],
    ["obtain Thunder Quartz ring +0, +1, +2, and +3",   "3+ O"],
    ["obtain Outcry",                           "4+ O"],
    ["obtain the Ivory Warrior Ring",           "4+ O"],
    ["obtain the Curved Nil Greatsword",        "4+ O"],
    ["obtain the Chime of Screams (Nadalia)",   "4+ O"],
    ["obtain Ring of Blades +0, +1, and +2",    "4+ O"],
    ["obtain Ring of the Living",               "4+ O"],
    ["obtain both Smelter Swords (blue and red)", "4+ O P"],

    # Tasks
    ["purchase the Smelter Demon set",		"1+ T P"],
    ["purchase the Lost Sinner set",        "1+ T P"],
    ["purchase the Looking Glass Knight set", 					"1+ T"],
    ["purchase all 4 pieces of the Moonlight Butterfly set", 	"2+ T P"],
    ["join the Heirs of the Sun",       	"012 T P"],
    ["join the Way of the Blue",        	"012 T P"],
    ["join the Bell Keepers",           	"0+ T P"],
    ["join the Company of Champions",   	"012 T P"],
    ["join the Rat King covenant",      	"1+ T P"],
    ["join the Brotherhood of Blood",   	"1+ T P"],
    ["join the Blue Sentinels",         	"1+ T P"],
    ["join the Pilgrims of Dark",       	"1+ T"],
    ["join the Dragon Remnants covenant", 	"1+ T"],
    ["upgrade a weapon to +10", "1+ T P"],
    ["spice a spell at Magerold", "123 T P"],
    ["use Gillian to place any ladder", "12 T P"],
    ["change the nature of your being", "1+ T P"],
    ["use a Pharros contraption to get wet", "1+ T P"],

    ["infuse a weapon",                 "01 T P"],  # trivial/easy specific
    ["purchase 3 different infusions",  "2 T P"],   # medium-specific
    ["purchase 4 different infusions",  "3 T P"],   # hard-specific
    ["purchase all infusions", 	        "4+ T P"],  # expert+

    ["get 4 estus flask uses",          "1 T P"],   # easy-specific
    ["get 6 estus flask uses",          "2 T P"],   # medium-specific
    ["get 7 estus flask uses",          "3+ T P"],  # hard+

    ["upgrade the estus flask to +2",   "1 T P"],   # easy-specific
    ["upgrade the estus flask to +4",   "1+ T P"],  # medium+

    ["level a stat to 69",              "1 T P"],   # easy-specific
    ["level a stat to 99",              "1+ T P"],  # medium+

    ["kill 3 invisible hollows",        "12 T P"],  # easy/medium
    ["kill 5 invisible hollows",        "3 T P"],   # hard-specific
    ["kill 7 invisible hollows",        "4 T P"],   # expert-specific
    ["kill 9 invisible hollows",        "5 T P"],   # torture-specific

    ["use 5 Pharros contraptions",      "123 T P"],  # easy-hard
    ["use 5 Pharros contraptions in 5 different locations", "4+ T P"],  # expert+

    ["start as deprived",               "1+ T P"],
    ["start as cleric",                 "1+ T P"],
    ["start as sorcerer",               "1+ T P"],
    ["start without a gift",            "1+ T P"],
    ["start deprived with no gift",     "4+ T P"],
    ["light all 5 bonfires in The Lost Bastile",            "1+ T P"],
    ["light all 4 bonfires in Drangleic Castle",            "1+ T"],
    ["light all 4 bonfires in Shrine of Amana",             "1+ T"],
    ["light all 4 bonfires in Forest of Fallen Giants",     "1+ T P"],
    ["ring the bells of both belfries",                     "1+ T P"],
    ["get unpoisoned by the Gutter bug",                    "123 T P"],
    ["trade one boss soul with each vendor",                "1+ T P"],

    ["drop 5 tradeable items in the bird's nest",           "12 T P"],  # easy/medium
    ["drop 20 tradeable items in the bird's nest",          "3 T P"],   # hard-specific
    ["drop 25 tradeable items in the bird's nest",          "4 T P"],   # expert-specific
    ["drop 30 tradeable items in the bird's nest",          "5 T P"],   # torture-specific

    ["trade 3 (non-invis-hollow dropped) Petrified Something at nest",    	"2+ T P"],
    ["grab the flame butterfly from atop the tree in Najka fight", 			"2+ T P"],
    ["reverse hollowing at the amana shrine",               "2+ T"],
    ["upgrade a pyro flame to +7",                          "2+ T"],
    ["deal the finishing blow to a boss using a ring of thorns", "2+ T P"],
    ["attune one of each type of spell at the same time",   "2+ T P"],

    ["traverse 3 fog walls from behind",                    "2 T P"],   # medium-specific
    ["traverse 4 fog walls from behind",                    "3 T P"],   # hard-specific
    ["traverse 5 fog walls from behind",                    "4+ T P"],  # expert+

    ["repair a weapon at the whipping tree",                "2+ T P"],
    ["talk to Gavlan in all 3 locations",                   "2+ T P"],
    ["have at least one of each arrow type in your inventory",          "2+ T"],
    ["have at least one of each great arrow type in your inventory",    "2+ T"],
    ["have at least one of each bolt type in your inventory",           "2+ T"],
    ["kill the Majula mimic (ng+)",                         "2+ T P"],
    ["activate the dragon in Aldia's Keep",                 "3+ T"],
    ["enter the fume knight fight wearing velstadts helm",  "3+ T"],
    ["cut off things from 3 different bosses",              "3+ T P"],
    ["upgrade a weapon with twinkling titanite to +5",      "3+ T P"],
    ["upgrade a weapon with petrified dragon bones to +5",  "3+ T P"],
    ["have all 6 resin types in your inventory",            "3+ T P"],

    ["kill 8 blue crystal lizards",                         "3 T P"],   # hard-specific
    ["kill 12 blue crystal lizards",                        "4 T P"],   # expert-specific
    ["kill 14 blue crystal lizards",                        "5 T P"],   # torture-specific

    ["have all 7 unique bomb/urn consumables in your inventory", "4+ T P"],
    ["invade and kill licia",               "4+ T"],
    ["get all gestures",                    "4+ T"],
    ["join all covenants",                  "4+ T"],

    ["parry 3 different bosses",            "2 T P"],   # medium-specific
    ["parry 4 different bosses",            "3 T P"],   # hard-specific
    ["parry 5 different bosses",            "4 T P"],   # expert-specific
    ["parry 6 different bosses",            "5 T P"],   # torture-specific

    ["light all 5 bonfires in Brume Tower", "4+ T P"],
    ["light all 5 bonfires in Eleum Loyce", "4+ T"],
    ["collect all 3 Eleum Loyce Knights",   "4+ T"],
    ["inherit Benhart's armour",            "4+ T"],
    ["inherit Lucatiel's armour",           "4+ T"],
    ["kill 4 bosses in Covenant of Champions", "4+ T P"],
    ["kill Gutter Denizen (gutter sconses)",                "4+ T P"],
    ["kill Greatsword Foreigner phantom (Things Betwitx)",  "4+ T P"],
    ["kill Velstadt wearing Fume set, Fume sword, and Fume Ultra Greatsword", "4+ T"],
    ["in dragon shrine, kill the first three giant warriors and kill all dragon dudes on the final stairs", "4+ T"],
    ["have all available NPCs alive in Majula together (gathering of exiles)", 	"4+ T P"],
    ["have all 11 unique lesser soul items in your inventory", 					"4+ T P"],
    ["return a strong heat to the crowns (4 crowns)",       "5 T"],
    ["obtain 60 unique rings (+0, +1 etc. doesn't count)",  "5 T"],
    ]
