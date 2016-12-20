import mtg_db_manager as db
import re

# markdown file to be read in
markdown_file = "..\\inventory.md"

# read in db
mtg_db = db.load_db()
mtg_cards = mtg_db.keys()

inventory_pattern = "^.{3,}\s\|\s\d{1,}$"
invalid_card_file = "invalid_names.csv"


# read in and validate markdown file
# the prints cards that are not valid
def print_invalid_cards(inventory_file, pattern, out_file):

    # opens a markdown file to read in card list
    inv_file = open(inventory_file, "r")

    # list to store invalid cards
    invalid_cards = []

    for line in inv_file:
        if re.search(pattern, line) is not None:
            # if matches inventory pattern

            # parse inventory file
            line_split = line.split(" | ")
            card_names = line_split[0].strip()
            card_qt = int(line_split[1].strip())

            # if a merged instant or sorcery from
            # return to ravnica, count them as separate
            # cards even though they are the same card
            card_names_list = []
            if " // " in card_names:
                card_names_split = card_names.split(" // ")
                for card in card_names_split:
                    card = card.strip()
                    card_names_list.append(card)
            else:
                card_names_list.append(card_names)

            # go through each card name and clean
            # then validate if in card db. If not
            # then print out invalid card names
            for card_name in card_names_list:
                # proper casing
                card_name = card_name.title()
                card_name = card_name.replace("  ", " ")
                card_name = card_name.replace(" A ", " a ")
                card_name = card_name.replace(" At ", " at ")
                card_name = card_name.replace("'S", "'s")
                card_name = card_name.replace(" In ", " in ")
                card_name = card_name.replace(" Into ", " into ")
                card_name = card_name.replace(" From ", " from ")
                card_name = card_name.replace(" To ", " to ")
                card_name = card_name.replace(" The ", " the ")
                
                card_name = card_name.replace("-O'-", "-o'-")
                card_name = card_name.replace(" By ", " by ")
                card_name = card_name.replace(" For ", " for ")
                card_name = card_name.replace(" Of ", " of ")
                card_name = card_name.replace(" And ", " and ")
                card_name = card_name.replace(" On ", " on ")
                card_name = card_name.replace(" Upon ", " upon ")
                card_name = card_name.replace(" With ", " with ")

                if card_name not in mtg_cards:
                    invalid_cards.append(card_name)

    inv_file.close()  # close the file

    out_file = open(out_file, "w")
    out_file.write("card_name\n")
    for card in invalid_cards:
        out_file.write("\"" + card + "\"\n")

    out_file.close()

print_invalid_cards(
    inventory_file=markdown_file,
    pattern=inventory_pattern,
    out_file=invalid_card_file)
