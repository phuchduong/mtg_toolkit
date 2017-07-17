# @title: merge_inv_with_tcg.R
# @author: Phuc Duong <phuchduong>
# @start_date: July 8th, 2017
# @email: phuchduong@hotmail.com
# description: merge inventory sheet with tcgplayer price list


import json
import pandas as pd

###############
# read in JSON
###############
i_filename = "mtg_card_db.json"
i_dir = "mtgjson/"

i_path = i_dir + i_filename

with open(i_path) as json_str:
    jdb = json.load(json_str)

mj_df = pd.read_json(i_path, orient="index")
mj_df.to_csv("mtg_db.csv")