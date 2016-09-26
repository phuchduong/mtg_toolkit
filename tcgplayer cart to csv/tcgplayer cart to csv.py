from bs4 import BeautifulSoup

html_file = "C:/Users/phuc/Downloads/temp tcg cart/card.html"

# Classes
card_n_set_class = "sellerWrapMarket"
rarity_n_condition_class = "detailsContents"
price_class = "priceBox"
quantity_class = "qtyBox"

# parses file
raw_html = open(html_file, 'r').read()
cart_soup = BeautifulSoup(raw_html, "html.parser")

# dictionary of cards
card_dict = {}

# Grab card and set
= cart_soup.find_all("div", class_=card_n_set_class)
= cart_soup.find_all("div", class_=rarity_n_condition_class)
= cart_soup.find_all("div", class_=price_class)
= cart_soup.find_all("div", class_=quantity_class)

# loops through each distributor
for distributor in distributors_sections:
