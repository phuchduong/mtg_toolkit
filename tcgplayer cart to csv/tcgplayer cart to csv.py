from bs4 import BeautifulSoup

html_file = "C:/Users/phuc/Downloads/temp tcg cart/card.html"
distributor_div = ["div", "class", "sellerWrapMarket"]

raw_html = open(html_file, 'r').read()
cart_soup = BeautifulSoup(raw_html, "html.parser")

cart_soup.find(distributor_div[0], {distributor_div[1]: distributor_div[2]})
cart_soup[0]
