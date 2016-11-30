import os
import json
from urllib.request import urlopen as uReq
import zipfile
from io import BytesIO

db_folder_name = "card_db"
db_file_name = "mtg_card_db.json"

current_dir = os.path.dirname(os.path.realpath(__file__))

# downloads the MTG json database to a sister directory.
def download_json_db():
    print("Calling function download_json_db()...\n")
    # this function requires....
    # from io import BytesIO
    # import zipfile
    # from urllib.request import urlopen as uReq
    # import os

    # fields
    host_url = 'https://mtgjson.com/json/AllCards.json.zip'
    internal_filename = 'AllCards.json'

    # downloads the file
    print("Downloading JSON library from mtgjson.com...")

    client = uReq(host_url)
    zip_byte_file = client.read()
    client.close()
    print("Download... Done!\n")

    # Extract the file
    print("Extracting zip folder....")
    zip_folder = zipfile.ZipFile(BytesIO(zip_byte_file))
    json_file = zip_folder.read(internal_filename)
    print("Extraction... Complete!\n")

    # makes folder if it does not exist
    if not os.path.isdir(db_folder_name):
        os.makedirs(db_folder_name)

    # writes the file to disk
    output_path = os.path.join(current_dir, db_folder_name, db_file_name)
    print("Writing to..." + output_path)
    file_writer = open(output_path, 'w')
    file_writer.write(str(json_file))
    print("Writing.... Complete!\n")


# Reads a json file in a sister directory
def load_json_file(folder_name, file_name):
    # this function requires....
    import os
    import json

    # Find MTG JSON DB
    # Your file structure should look like this
    #
    # + exploration_and_experimentation <-- current directory
    # | -- name_vs_keyname.py           <-- current file
    # + mtg_json                        <-- file dir
    # | -- mtg_card_db.json             <-- target file
    #

    file_path = os.path.join(current_dir, "..", folder_name, file_name)

    # Ingress
    json_file = json.loads(open(file_path).read())

    return(json_file)

# Read in the JSON Library
# mtg_db = load_json_file(folder_name=db_folder_name, file_name=db_file_name)
# print(str(mtg_db.keys()).encode("utf-8"))

# view the difference between the key and name
#   def view_difference():
