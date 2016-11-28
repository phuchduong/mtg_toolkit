import json
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = "mtg_card_db.json"


mtg_db = json.loads(open(file_name).read())

# sorts by the color wheel
wubrg_order = {
    "W": 0,  # white
    "U": 1,  # blue
    "B": 2,  # black
    "R": 3,  # red
    "G": 4   # green
}

# sort by alara shards, then tarkir guilds.
tri_color_order = [
    "WUG",
    "WUB",
    "UBR",
    "BRG",
    "WRG",
    "WBG",
    "WUR",
    "WBR",
    "UBG",
    "URG"
]
tri_color_title = {
    "WUG": "Bant",
    "WUB": "Esper",
    "UBR": "Grixis",
    "BRG": "Jund",
    "WRG": "Naya",
    "WBG": "Abzan",
    "WUR": "Jeskai",
    "WBR": "Mardu",
    "UBG": "Sultai",
    "URG": "Temur"
}
super_type_ordering = [
    'Creature',
    'Enchantment',
    'Planeswalker',
    'Sorcery',
    'Instant',
    'Artifact',
    'Land'
]


def query_by_number_of_colors(card_db, num_of_colors):
    # returns a list of card names that have the desired
    #    number of colors in their color identidy.
    # card_db = MTG json of cards, as dict
    # num_of_colors = int number of colors to select
    #   between 1 and 5
    # Colorless is not yet supported

    card_list = []  # list to be returned.
    for card_name in card_db:
        card_dict = card_db[card_name]
        if("colorIdentity" in card_dict.keys()):
            # Colorless cards do not have color identidy
            if(len(card_dict["colorIdentity"]) == num_of_colors):
                if(card_name not in card_list):
                    card_list.append(card_name)
    return card_list


def bucket_by_tricolor(card_db):
    # Buckets the number of cards by distinct tri-color
    #     combinations.
    tri_color = query_by_number_of_colors(
        card_db=mtg_db,
        num_of_colors=3
    )
    tri_color_dict = {}

    for card_name in tri_color:
        color_identidy_list = mtg_db[card_name]['colorIdentity']
        # sort color string by wubrg color order
        color_identidy_list.sort(key=lambda val: wubrg_order[val[0]])
        color_type_key = "".join(color_identidy_list)

        # Creates a color grouping if there is not
        if color_type_key not in tri_color_dict:
            tri_color_dict[color_type_key] = {}

        # Adds a dictionary key
        if "Creature" in mtg_db[card_name]["types"]:
            # Creature superceeds all other typings
            super_type = "Creature"
        else:
            super_type = mtg_db[card_name]["types"][0]

        # Adds key to the color group
        if super_type not in tri_color_dict[color_type_key]:
            tri_color_dict[color_type_key][super_type] = []
        tri_color_dict[color_type_key][super_type].append(card_name)
    # Sort cards alphabetically within supertype.
    for shard in tri_color_dict:
        for supertype in tri_color_dict[shard]:
            tri_color_dict[shard][supertype].sort()
    return tri_color_dict


def print_markdown(sorted_card_dict):
    guid = datetime_guid()
    filename = "tricolor" + guid + ".md"
    with open(filename, 'wt') as f:
        # f.write(sorted_card_dict.keys())
        # prints what's inside.
        for shard in tri_color_order:
            title = tri_color_title[shard]
            color_title = color_combination_string(shard)
            f.write("## " + color_title + ", " + title + "\n")
            for super_type in super_type_ordering:
                if super_type in card_dict[shard]:
                    f.write("### " + super_type + " < " + title + "\n")
                    f.write("Card | Qt" + "\n")
                    f.write("--- | ---" + "\n")
                    cards = card_dict[shard][super_type]
                    for card in cards:
                        f.write(str(card) + " | " + "\n")


# Returns a string guid of the current time.
# July 3rd 2016, 3:28:46 am -> 160703032846
def datetime_guid():
    i = datetime.datetime.now()
    return i.strftime('%y%m%d%H%M%S')


# Translates color keys letters to strings
def color_combination_string(color_key):
    color_dict = {
        "C": "Colorless",
        "W": "White",
        "U": "Blue",
        "B": "Black",
        "R": "Red",
        "G": "Green"
    }
    color_list = []
    for color in color_key:
        color_list.append(color_dict[color])
    color_string = " + ".join(color_list)
    return color_string


card_dict = bucket_by_tricolor(card_db=mtg_db)
print_markdown(card_dict)

# print(",".join(print_output).encode('utf-8'))
input("Press Enter to close...")
