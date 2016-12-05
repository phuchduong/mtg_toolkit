import mtg_db_manager as db

# db.download_json_db()
mtg_db = db.load_json_file()

card_names = mtg_db.keys()

card_names = sorted(card_names)

# building headers
headers = []
for card_name in card_names:
    for header in mtg_db[card_name]:
        if header not in headers:
            headers.append(header)

# writes file
f.open
for card_name in card_names:
