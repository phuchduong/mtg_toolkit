from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

# Url of page to scrape
my_url = "http://magic.wizards.com/en/events/coverage/gpman16/mono-blue-prison-with-martin-muller-2016-05-28"

# Grab page html form URL
web_client = uReq(my_url)

# convert raw html to a soup object
page_soup = BeautifulSoup(web_client.read(), "html.parser")

# Extract deck
deck_soup = page_soup.find_all("div", {"class": "deck-list-text"})

# Extract card count quantities from deck
card_counts = page_soup.find_all("a", {"class": "card-name"})
# Extract card information from deck

input("Press any key to end.")
