from bs4 import BeautifulSoup

html_file = "C:/Users/phuc/Downloads/temp tcg cart/card.html"

# Classes
card_n_set_class = "itemsContents"
rarity_n_condition_class = "detailsContents"
price_class = "priceBox"
quantity_class = "qtyBox"

# parses file
raw_html = open(html_file, 'r').read()
cart_soup = BeautifulSoup(raw_html, "html.parser")

# dictionary of cards
card_dict = {}

# Grab card and set
card_n_set_rs = cart_soup.find_all("div", class_=card_n_set_class)
for block in card_n_set_rs:
    card_name = block.h3.a.string
    card_set =  block.p.string.replace(" - Magic", "")

    card_dict[card_name] = {}
    card_dict[card_name]["set"] = card_set

    # finds rarity and condition of card
    rarity_n_condition_rs = cart_soup.find_all("div", class_=rarity_n_condition_class)
    for block in rarity_n_condition_rs:
        rarity = block.p.string.replace("Rarity: ", "")


# price_rs = cart_soup.find_all("div", class_=price_class)
# for block in price_rs:


# quantity_rs = cart_soup.find_all("div", class_=quantity_class)
# for block in quantity_rs:



# loops through each distributor
# for distributor in distributors_sections:

print(card_dict)
