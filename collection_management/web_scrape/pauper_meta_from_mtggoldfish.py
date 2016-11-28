from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import datetime

pauper_urls = "http://www.mtggoldfish.com/metagame/pauper#paper"
mtggoldfish_url = "http://www.mtggoldfish.com/archetype/pauper-stompy-22958#paper"

def parse_deck(mtggoldfish_url):
    # grab and soup page
    page_client = uReq(mtggoldfish_url)
    print("Grabbing the html through the blind eternities...")
    page_soup = BeautifulSoup(
        page_client.read(), "html.parser"
    )
    page_client.close()

    # Grabs the paper decklist with the prices
    print("Extracting table...")
    deck_table = page_soup.find_all(
        "div", {"id": "tab-paper"}
    )

    # discards things around the table
    deck_table = deck_table[0].div.div.table

    # gets all the rows from the html table
    table_rows = deck_table.find_all("tr")

    decklist = {}

    # Loops through the rows
    print("Parsing rows...")
    for row in table_rows:
        columns = row.find_all("td")
        if(len(columns) == 4):
            # extracts features from each column
            quantity = columns[0].text.strip()
            card_name = columns[1].text.strip()
            color = ""
            try:
                color = columns[2].span.img['alt'].strip()
            except AttributeError:
                pass
            price = round(
                float(
                    columns[3].text.strip()
                ),
                2  # two decimal places
            )
            card_key = card_name.lower()

            decklist[card_key] = {
                "card_name": card_name,
                "color": color,
                "price_amt": price,
                "price_date_utc": str(datetime.datetime.utcnow()),
                "deck_qty": quantity,
            }
            print("Parsed..." +
                  card_name + ", " +
                  color + ", " +
                  quantity + ", " +
                  str(price)
                  )
    print("Printing card names.")
    card_names = list(decklist.keys())
    card_names.sort()
    print(card_names)
    print("Printing dictionary.")
    print(decklist)
parse_deck(mtggoldfish_url)
input("Press enter to close the script.")
