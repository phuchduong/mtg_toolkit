# @title: update_mtg_json.py
# @author: Phuc Duong <phuchduong>
# @start_date: July 9th, 2017
# @email: phuchduong@hotmail.com
# description: manages the mtg json file.

import json
from urllib.request import urlopen as uReq
import zipfile
from io import BytesIO

db_file_name = "mtg_card_db.json"


# downloads the MTG json database to a sister directory.
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

# Converts to JSON
json_file = json_file.decode("utf-8")
json_file = json.loads(json_file)
json_file = json.dumps(json_file)

print("Extraction... Complete!\n")

# writes the file to disk
print("Writing file...")
file_writer = open(db_file_name, 'w')
file_writer.write(json_file)
file_writer.close()
print("Writing.... Complete!\n")
