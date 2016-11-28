import os
import json

db_folder_name = "mtg_json"
db_file_name = "mtg_card_db.json"


# Reds a json file in a sister directory
def load_json_file(folder_name, file_name):
    # Find MTG JSON DB
    # Your file structure should look like this
    #
    # + exploration_and_experimentation <-- current directory
    # | -- name_vs_keyname.py           <-- current file
    # + mtg_json                        <-- file dir
    # | -- mtg_card_db.json             <-- target file
    #
    current_dir = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(current_dir, "..", folder_name, file_name)

    # Ingress
    json_file = json.loads(open(file_path).read())

    return(json_file)


mtg_db = load_json_file(folder_name=db_folder_name, file_name=db_file_name)

print(str(mtg_db.keys()).encode("utf-8"))
# view the difference between the key and name
#   def view_difference():
