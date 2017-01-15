import mtg_db_manager as db
import re
import os


def main():

    # load in mtg db
    mtg_db = db.load_db()

    # parse inventory file
    markdown_file = "..\\inventory.md"
    inventory = parse_inv_file(filename=markdown_file)

    # cleans, conforms, validates card names
    inventory = clean_card_names(
        inventory=inventory, card_db=mtg_db.keys())
    print(inventory)


# cleans, comforms, validates card names
def clean_card_names(inventory, card_db):
    # current working directory
    cwd = os.getcwd()

    # new dictionary of inventory
    # but with cleaned and validated
    # card names
    new_inv = {}

    # list to store invalid card names.
    # to be printed as a log file.
    invalid_cards = []
    invalid_cards_filename = "invalid_names.csv"
    invalid_filepath = cwd + invalid_cards_filename

    # mispelled card names and their
    # corrections
    cms = load_mispelled_words()

    # go through each card name and clean
    # then validate if in card db. If not
    # then print out invalid card names
    for card_name in inventory:
        quantity = inventory[card_name]

        # proper casing
        card_name = proper_case(card_name)

        # if card does not appear in card db,
        # then its invalid. Correct for mispelling
        # if a corection exists using the cms
        # (commonly mispelled)
        if card_name not in card_db:
            # searchs for a mispelling and corrects if there is
            for mispelling in cms:
                card_name = card_name.replace(
                    mispelling, cms[mispelling])

            # card still has no valid name in db
            if card_name not in card_db:
                invalid_cards.append(card_name)

        # builds new dictionary with validated names
        new_inv[card_name] = quantity

    # writes invalid cards to a file
    out_file = open(invalid_filepath, "w")
    out_file.write("card_name\n")
    for card in invalid_cards:
        # print(card)
        out_file.write("" + card + "\n")
    out_file.close()

    return new_inv


# Takes in a string, proper cases it, then
# returns the changed string.
def proper_case(text):
    text = text.title()
    text = text.replace("  ", " ")
    text = text.replace(" A ", " a ")
    text = text.replace(" At ", " at ")
    text = text.replace("'S", "'s")
    text = text.replace(" In ", " in ")
    text = text.replace(" Into ", " into ")
    text = text.replace(" From ", " from ")
    text = text.replace(" To ", " to ")
    text = text.replace(" The ", " the ")
    text = text.replace("-O'-", "-o'-")
    text = text.replace(" By ", " by ")
    text = text.replace(" For ", " for ")
    text = text.replace(" Of ", " of ")
    text = text.replace(" And ", " and ")
    text = text.replace(" On ", " on ")
    text = text.replace(" Upon ", " upon ")
    text = text.replace(" With ", " with ")
    return text


# deprecated
# read in and validate markdown file
# the prints cards that are not valid
def print_invalid_cards(inventory_file, pattern, out_file):

    # list to store invalid cards
    invalid_cards = []

    # mispelled card names and their
    # corrections
    cms = load_mispelled_words()

    # go through each card name and clean
    # then validate if in card db. If not
    # then print out invalid card names
    for card_name in card_names_list:

        # if card does not appear in card db,
        # then its invalid. Correct for mispelling
        if card_name not in mtg_cards:
            print("before: " + card_name)
            for mispelling in cms:
                # print("card_name:       " + card_name)
                # print("mispelling:      " + mispelling)
                # print("cms[mispelling]: " + cms[mispelling])
                card_name = card_name.replace(mispelling, cms[mispelling])
            print("after:  " + card_name)
            print("\r")
            if card_name not in mtg_cards:
                print("invalid card: " + card_name)
                invalid_cards.append(card_name)

    inv_file.close()  # close the file

    # writes invalid cards to a file
    out_file = open(out_file, "w")
    out_file.write("card_name\n")
    for card in invalid_cards:
        # print(card)
        out_file.write("" + card + "\n")
    out_file.close()


# loads a list of commonly mispelled names
# and their corrections. returns a dictionary
# of commonly mispelled words and its corections.
def load_mispelled_words():
    # cms: commonly mispelled

    # current working directory
    cwd = os.getcwd()
    # markdown file to be read in
    cms_filename = r"\reference_files\common_mispellings.csv"
    # opens mispelled workds file
    cms_file = open(cwd + cms_filename, "r")

    cms = {}
    next(cms_file)  # skips first line
    for entry in cms_file:
        # builds a dictionary where
        # the key is the mispelling
        # and the value is the replacement
        # correction
        cms_split = entry.split("\t")
        mispelled = cms_split[0]
        correction = cms_split[1].replace("\n", "")
        cms[mispelled] = correction
    return cms


# parses an inventory file that was
# in markdown format
def parse_inv_file(filename):
    inventory = {}

    inventory_pattern = "^.{3,}\s\|\s\d{1,}$"

    # opens a markdown file to read in card list
    inv_file = open(filename, "r")

    for line in inv_file:
        if re.search(inventory_pattern, line) is not None:
            # if matches inventory pattern

            # parse inventory line
            print(line)
            line_split = line.split(" | ")
            card_names = line_split[0].strip()
            card_qt = int(line_split[1].strip())

            # if a merged instant or sorcery from
            # return to ravnica, count them as separate
            # cards even though they are the same card
            card_names_list = []
            if " // " in card_names:
                card_names_split = card_names.split(" // ")
                for card in card_names_split:
                    card = card.strip()
                    card_names_list.append(card)
            else:
                card_names_list.append(card_names)

            for card_name in card_names_list:
                inventory[card_name] = card_qt
    inv_file.close()  # close the file

    return inventory


# executes script
main()
