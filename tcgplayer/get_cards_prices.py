# @title: get_card_prices.py
# @author: Phuc Duong <phuchduong>
# @start_date: July 7th, 2017
# @email: phuchduong@hotmail.com
# description: scrapes all every card pricing information off tcgplayer by set

from bs4 import BeautifulSoup as soup       # html data structure
from urllib.request import urlopen as uReq  # web client
from urllib.request import quote            # encoder
from urllib.request import Request          # encoder
import pandas as pd                         # data frame structure
from datetime import datetime               # clock

# read in existing csv table
df = pd.read_csv("tcg_prices.csv")
before = len(df)        # last row index +1
cur_index = len(df)     # last row index +1

# spoofing a user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"

###################################
# read in list of sets
###################################
sets = pd.read_csv("set_names.csv")
sets = sets.fillna("")

# finds the first "not done" set to scrape
not_done = sets["status"] != "done"
set_name = sets[not_done].iloc[0]["set_name"]


print("parsing... " + set_name)


###################################
# form url
###################################

set_name_url = quote(set_name)   # encode html escape characters

root_url = "http://magic.tcgplayer.com/db/search_result.asp?Set_Name="

set_url = root_url + set_name_url

print("url: " + set_url)

# spoof header
req = Request(set_url)
req.add_header("User-Agent", "Mozilla/5.0")


###################################
# download and parse page into soup
###################################

scrape_date = str(datetime.now())
web_client = uReq(req)
print("web_client: " + str(web_client.getcode()))

soup = soup(web_client.read(), "html.parser")
web_client.close()


#######################
# isolate pricing table
#######################

html_tables = soup.find_all("table")

# lots of tables. We only need the pricing table
html_table = html_tables[8]


#######################
# parse table
#######################
rows = html_table.find_all("tr")

for row in rows:
    # for each row, parse each cell

    cells = row.find_all("td")

    # parse each cell
    card_name = cells[0].text.strip()
    mana_cost = cells[1].text.strip()
    set_name = cells[2].text.strip()
    rarity = cells[3].text.strip()
    price_h = cells[4].text.strip()
    price_m = cells[5].text.strip()
    price_l = cells[6].text.strip()

    # add row to data frame
    df.loc[cur_index] = [
        card_name,
        mana_cost,
        set_name,
        rarity,
        price_h,
        price_m,
        price_l,
        scrape_date
    ]
    cur_index += 1

# how many rows were added?
diff = cur_index - before
print("data size: +" + str(diff) + " rows added.")

# writes to csv
df.to_csv("tcg_prices.csv", index=False)

##############################################
# mark set as completed in set_names.csv file
##############################################

# grabs the first index, after the filter,
# which is the actual index of the row
act_index = sets[not_done].iloc[0].name
sets = sets.set_value(act_index, "status", "done")
print(set_name + " is marked as complete.")
sets.to_csv("set_names.csv", index=False)
