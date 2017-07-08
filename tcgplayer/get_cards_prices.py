# @title: get_card_prices.py
# @author: Phuc Duong <phuchduong>
# @start_date: July 7th, 2017
# @email: phuchduong@hotmail.com
# description: scrapes all every card pricing information off tcgplayer by set

from bs4 import BeautifulSoup as soup       # html data structure
from urllib.request import urlopen as uReq  # web client
from urllib.request import quote            # encoder
import pandas as pd                         # data frame structure
from datetime import datetime               # clock

###################################
# initialize data frame
###################################
df = pd.DataFrame(
    columns=(
        "card_name",
        "mana_cost",
        "set_name",
        "rarity",
        "price_h",
        "price_m",
        "price_l"
    )
)
cur_index = 1

###################################
# form url
###################################
set_name = "battle for zendikar"

set_name = quote(set_name)

###################################
# download and parse page into soup
###################################

form_url = "http://magic.tcgplayer.com/db/search_result.asp?Set_Name=battle%20for%20zendikar"

scrape_date = str(datetime.now())
web_client = uReq(form_url)

soup = soup(web_client.read(), "html.parser")

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
        price_l
    ]
    cur_index += 1

# add scrape date to each entry
df["scrape_date"] = scrape_date

df.to_csv("tcg_prices.csv", index=False)
