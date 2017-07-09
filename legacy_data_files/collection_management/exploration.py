import mtg_db_manager as db

# db.download_json_db()
mtg_db = db.load_json_file()

card_names = mtg_db.keys()

card_names = sorted(card_names)

# building headers
headers = []
f = open("card_names.csv", "w")
f.write("Card_Name\n")
for card_name in card_names:
    f.write(card_name + "\n")

f.close()
