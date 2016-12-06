import mtg_db_manager as db

# markdown file to be read in
markdown_file = "..\\inventory.md"

# read in db
mtg_db = db.load_json_file()
mtg_cards = mtg_db.keys()


# read in and validate markdown file
def validate_inventory_md(filename):
    f = open(filename, "r")
    for line in f:
        print(line)

validate_inventory_md(filename=markdown_file)
