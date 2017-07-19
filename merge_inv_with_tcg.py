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

#################################
# breaking down cards by type
#################################
# converts column to string from object, cast to lower case
mj_df["types"] = mj_df["types"].astype(str).str.lower()
# removes brackets and quotes before and after
mj_df["types"] = mj_df["types"].str.replace("\['", "").str.replace("\']", "")

mj_df["isArtifact"] = mj_df["types"].str.contains("artifact")
mj_df["isCreature"] = mj_df["types"].str.contains("creature")
mj_df["isEnchantment"] = mj_df["types"].str.contains("enchantment")
mj_df["isInstant"] = mj_df["types"].str.contains("instant")
mj_df["isLand"] = mj_df["types"].str.contains("land")
mj_df["isPlaneswalker"] = mj_df["types"].str.contains("planeswalker")
mj_df["isSorcery"] = mj_df["types"].str.contains("sorcery")

#################################
# breaking down cards by sub type
#################################
# converts column to string from object, cast to lower case
mj_df["subtypes"] = mj_df["subtypes"].astype(str).str.lower()
# removes brackets and quotes before and after
mj_df["subtypes"] = mj_df["subtypes"].str.replace("\['", "").str.replace("\']", "")

mj_df["isEquipment"] = mj_df["subtypes"].str.contains("equipment")
mj_df["isAura"] = mj_df["subtypes"].str.contains("aura")
mj_df["isVehicle"] = mj_df["subtypes"].str.contains("vehicle")

# clean color identidy
mj_df["colorIdentityStr"] = mj_df["colorIdentity"]
mj_df["colorIdentityStr"] = mj_df["colorIdentityStr"].astype(str)
mj_df["colorIdentityStr"] = mj_df["colorIdentityStr"].str.replace("\['", "").str.replace("\']", "").str.replace("\'", "")

# creates a feature based on the count number of colors
mj_df["color_count"] = mj_df["colorIdentityStr"].str.split(",").str.len()

# sorts the color identities
for i in range(0, len(mj_df) - 1):
    if type(mj_df.colorIdentity.iloc[i]) is list:
        mj_df.colorIdentity.iloc[i].sort()

# cleans the color identity
mj_df["colorIdentity"] = mj_df.colorIdentity.astype(str)
mj_df["colorIdentity"] = mj_df.colorIdentity.str.replace("\['", "").str.replace("\']", "").str.replace("\'", "")

# assigns a sorting number based on WUBRG order
# creates a column called wubrg order
mj_df["wubrg_order"] = -1
mj_df.loc[
    (mj_df["colorIdentity"] == "nan") &
    (
        (mj_df["layout"] == "normal") |
        (mj_df["layout"] == "double-faced")
    ),
    ("wubrg_order")
] = 0                                                           # Colorless
mj_df.loc[mj_df.colorIdentity == "W", ("wubrg_order")] = 1               # White
mj_df.loc[mj_df.colorIdentity == "U", ("wubrg_order")] = 2               # Blue
mj_df.loc[mj_df.colorIdentity == "B", ("wubrg_order")] = 3               # Black
mj_df.loc[mj_df.colorIdentity == "R", ("wubrg_order")] = 4               # Red
mj_df.loc[mj_df.colorIdentity == "G", ("wubrg_order")] = 5               # Green
mj_df.loc[mj_df.colorIdentity == "U, W", ("wubrg_order")] = 6            # Azorious
mj_df.loc[mj_df.colorIdentity == "R, W", ("wubrg_order")] = 7            # Boros
mj_df.loc[mj_df.colorIdentity == "B, U", ("wubrg_order")] = 8            # Dimir
mj_df.loc[mj_df.colorIdentity == "B, G", ("wubrg_order")] = 9            # Golgari
mj_df.loc[mj_df.colorIdentity == "G, R", ("wubrg_order")] = 10           # Gruul
mj_df.loc[mj_df.colorIdentity == "R, U", ("wubrg_order")] = 11           # Izzet
mj_df.loc[mj_df.colorIdentity == "B, W", ("wubrg_order")] = 12           # Orzhov
mj_df.loc[mj_df.colorIdentity == "B, R", ("wubrg_order")] = 13           # Rakdos
mj_df.loc[mj_df.colorIdentity == "G, W", ("wubrg_order")] = 14           # Selesnya
mj_df.loc[mj_df.colorIdentity == "G, U", ("wubrg_order")] = 15           # Simic
mj_df.loc[mj_df.colorIdentity == "B, G, W", ("wubrg_order")] = 16        # Abzan
mj_df.loc[mj_df.colorIdentity == "G, U, W", ("wubrg_order")] = 17        # Bant
mj_df.loc[mj_df.colorIdentity == "B, U, W", ("wubrg_order")] = 18        # Esper
mj_df.loc[mj_df.colorIdentity == "B, R, U", ("wubrg_order")] = 19        # Grixis
mj_df.loc[mj_df.colorIdentity == "R, U, W", ("wubrg_order")] = 20        # Jeskai
mj_df.loc[mj_df.colorIdentity == "B, G, R", ("wubrg_order")] = 21        # Jund
mj_df.loc[mj_df.colorIdentity == "B, R, W", ("wubrg_order")] = 22        # Mardu
mj_df.loc[mj_df.colorIdentity == "G, R, W", ("wubrg_order")] = 23        # Naya
mj_df.loc[mj_df.colorIdentity == "B, G, U", ("wubrg_order")] = 24        # Sultai
mj_df.loc[mj_df.colorIdentity == "G, R, U", ("wubrg_order")] = 25        # Temur
mj_df.loc[mj_df.colorIdentity == "B, G, R, U", ("wubrg_order")] = 26     # White-less
mj_df.loc[mj_df.colorIdentity == "B, G, R, W", ("wubrg_order")] = 27     # Blue-less
mj_df.loc[mj_df.colorIdentity == "G, R, U, W", ("wubrg_order")] = 28     # Black-less
mj_df.loc[mj_df.colorIdentity == "B, G, U, W", ("wubrg_order")] = 29     # Red-less
mj_df.loc[mj_df.colorIdentity == "B, R, U, W", ("wubrg_order")] = 30     # Green-less
mj_df.loc[mj_df.color_count == 5, ("wubrg_order")] = 31  # 5 color

# categorizes normal mtg cards from specialty cards like vanguard, tokens, schemes, and  planes


mj_df.to_csv("mtg_db.csv", index=False)
