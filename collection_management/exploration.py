import mtg_db_manager as db

# db.download_json_db()
mtg_db = db.load_json_file()

card_name = mtg_db.keys()

print(card_name)
