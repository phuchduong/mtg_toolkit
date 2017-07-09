from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

# URL to be scraped. Has to be an edhrec page.
target_url = "https://edhrec.com/sets/akh/"

# Open connection, download page
web_client = uReq(target_url)

# Parse page into a soup data structure
print("Grabbing website: " + target_url)
page_soup = BeautifulSoup(web_client.read(), "html.parser")

# Close the web client
web_client.close()

card_frames = page_soup.find_all("div", {"class": "nw"})

out_filename = "scrape_edhrec_output.tsv"
f = open(out_filename, "w")
headers = "card_name\tin_decks\tprice\n"
f.write(headers)

for card_frame in card_frames:
    name_frame = card_frame.find_all("div", {"class": "nwname"})
    card_name = name_frame[0].text

    quantity_frame = card_frame.find_all("div", {"class": "nwdesc ellipsis"})
    quantity = quantity_frame[0].text
    quantity = quantity.replace(" decks", "")

    price_frame = card_frame.find_all("a", {"alt": "Buy at Card Kingdom"})
    if(len(price_frame) > 0):
        price = price_frame[0].text
        price = price.strip()
    else:
        price = ""
    print("Writing... " + card_name + "\t" + quantity + "\t" + price)
    f.write(card_name + "\t" + quantity + "\t" + price + "\n")
f.close()
input("Done. Press any key to end.")
