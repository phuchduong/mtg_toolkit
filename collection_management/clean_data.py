import mtg_db_manager as db
import re

# markdown file to be read in
markdown_file = "..\\inventory.md"

# read in db
mtg_db = db.load_json_file()
mtg_cards = mtg_db.keys()


# read in and validate markdown file
# the prints cards that are not valid
def validate_inventory_md(filename):
    inventory_pattern = "^.{3,}\s\|\s\d{1,}$"
    # search_bot = re.compile(inventory_pattern)

    f = open(filename, "r")

    for line in f:
        if re.search(inventory_pattern, line) is not None:
            # if matches inventory pattern

            # parse inventory file
            line_split = line.split(" | ")
            card_name = line_split[0]
            card_qt = line_split[1]
            if card_name not in mtg_cards:
                print(card_name)

validate_inventory_md(filename=markdown_file)
