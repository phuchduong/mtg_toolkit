import json

file_name = "mtg_card_db.json"

mtg_db = json.loads(open(file_name).read())

def query_by_number_of_colors(card_db, num_of_colors):
    # returns only cards that have the number of specified
    #    colors.
    # card_db = MTG json of cards, as dict
    # num_of_colors = int number of colors to select
    #   between 0 and 5

    card_list = {}
    for card_name in card_db:
        # print(card_name.encode('utf-8'))
        card_dict = card_db[card_name]
        if("colorIdentity" in card_dict.keys()):
            if(len(card_dict["colorIdentity"]) == num_of_colors):
                card_name = card_dict["name"]
                print(card_name.encode('utf-8'))
                super_types = card_dict["types"]

                color_identidy = card_dict["colorIdentity"]
                card_list[card_name] = {
                    "super_types": super_types,
                    "color_identidy": color_identidy
                }
                if("subtypes" in card_dict.keys()):
                    card_list[card_name]["sub_types"] = card_dict["subtypes"]

    return card_list

print_output = query_by_number_of_colors(
    card_db=mtg_db,
    num_of_colors=5
)

print(",".join(print_output).encode('utf-8'))
print(print_output["Realm Razer"])
input("Press Enter to close...")
