import requests
from bs4 import BeautifulSoup


def get_battle_decks():
    return [
        ('Aether Flux', 'http://tappedout.net/mtg-decks/aether-flux-3/'),
        ('Ally Rally', 'http://tappedout.net/mtg-decks/23-09-16-jTa-ally-rally/'),
        ('Aura Blight', 'http://tappedout.net/mtg-decks/24-09-16-aura-blight/'),
        ('Battle Blitz', 'http://tappedout.net/mtg-decks/24-09-16-battle-blitz/'),
        ('Big Red Relics', 'http://tappedout.net/mtg-decks/big-red-relics-1/'),
        ('Black Death', 'http://tappedout.net/mtg-decks/24-09-16-black-death/'),
        ('Black Metal', 'http://tappedout.net/mtg-decks/30-05-17-black-metal/'),
        ('Blaze Brigade', 'http://tappedout.net/mtg-decks/blaze-brigade-2/'),
        ('Blood Brothers', 'http://tappedout.net/mtg-decks/23-09-16-NHq-blood-brothers/'),
        ('Blue Skies', 'http://tappedout.net/mtg-decks/24-09-16-blue-skies/'),
        ('Body Snatchers', 'http://tappedout.net/mtg-decks/body-snatchers-4/'),
        ('Brood Rites', 'http://tappedout.net/mtg-decks/brood-rites-4/'),
        ('Brutal Nursery', 'http://tappedout.net/mtg-decks/brutal-nursery-3/'),
        ('Brutal Truth', 'http://tappedout.net/mtg-decks/brutal-truth-1/'),
        ('Celestial Brood', 'http://tappedout.net/mtg-decks/07-08-17-celestial-brood/'),
        ('Chimera Flash', 'http://tappedout.net/mtg-decks/24-09-16-chimera-flash/'),
        ('Claws and Effect', 'http://tappedout.net/mtg-decks/claws-and-effect-4/'),
        ('Cold Front', 'http://tappedout.net/mtg-decks/07-08-17-cold-front/'),
        ('Consume the Weak', 'http://tappedout.net/mtg-decks/consume-the-weak-4/'),
        ('Converging Domains', 'http://tappedout.net/mtg-decks/07-08-17-converging-domains/'),
        ('Counter Revolution', 'http://tappedout.net/mtg-decks/07-08-17-counter-revolution/'),
        ('Dark Delve', 'http://tappedout.net/mtg-decks/24-09-16-dark-delve/'),
        ('Day of Doom', 'http://tappedout.net/mtg-decks/13-12-17-day-of-doom/'),
        ('Delirium Weaver', 'http://tappedout.net/mtg-decks/delirium-weaver-2/'),
        ('Dino Might', 'http://tappedout.net/mtg-decks/13-12-17-dino-might/'),
        ('Drone Strike', 'http://tappedout.net/mtg-decks/24-09-16-drone-strike/'),
        ('Emerging Evil', 'http://tappedout.net/mtg-decks/emerging-evil-3/'),
        ('Enchantress Blossom', 'http://tappedout.net/mtg-decks/enchantress-blossom-3/'),
        ('Firing Squad', 'http://tappedout.net/mtg-decks/07-08-17-firing-squad/'),
        ('Flight Club', 'http://tappedout.net/mtg-decks/07-08-17-flight-club/'),
        ('Golgari Graverobbers', 'http://tappedout.net/mtg-decks/golgari-graverobbers-2/'),
        ('Grave Tide', 'http://tappedout.net/mtg-decks/grave-tide-3/'),
        ('Grease Monkeys', 'http://tappedout.net/mtg-decks/07-08-17-grease-monkeys/'),
        ('Grim Constellation', 'http://tappedout.net/mtg-decks/grim-constellation-2/'),
        ('Grow-Bots!', 'http://tappedout.net/mtg-decks/grow-bots-4/'),
        ('Hatchet Men', 'http://tappedout.net/mtg-decks/hatchet-men-4/'),
        ('Heroes of Old', 'http://tappedout.net/mtg-decks/heroes-of-old-2/'),
        ('Impact Slide', 'http://tappedout.net/mtg-decks/impact-slide-1/'),
        ('Intangible Tokens', 'http://tappedout.net/mtg-decks/24-09-16-intangible-tokens/'),
        ('Invasive Bond', 'http://tappedout.net/mtg-decks/invasive-bond-2/'),
        ('Jungle Rumble', 'http://tappedout.net/mtg-decks/jungle-rumble-4/'),
        ('Kami Army', 'http://tappedout.net/mtg-decks/kami-army-3/'),
        ('Land Brawl', 'http://tappedout.net/mtg-decks/land-brawl/'),
        ('Mad House', 'http://tappedout.net/mtg-decks/mad-house-4/'),
        ('Manic Fog', 'http://tappedout.net/mtg-decks/manic-fog-1/'),
        ('Marsh Madness', 'http://tappedout.net/mtg-decks/marsh-madness-2/'),
        ('Monumental Force', 'http://tappedout.net/mtg-decks/monumental-force-4/'),
        ('Nature of the Beast', 'http://tappedout.net/mtg-decks/13-12-17-nature-of-the-beast/'),
        ('Necromancer\'s pact', 'http://tappedout.net/mtg-decks/necromancers-pact-3/'),
        ('Plow The Sands', 'http://tappedout.net/mtg-decks/plow-the-sands/'),
        ('Pristine Control', 'http://tappedout.net/mtg-decks/24-09-16-pristine-control/'),
        ('Reanimaniacs', 'http://tappedout.net/mtg-decks/07-08-17-reanimaniacs/'),
        ('rebel riot', 'http://tappedout.net/mtg-decks/rebel-riot-3/'),
        ('Red Menace', 'http://tappedout.net/mtg-decks/24-09-16-red-menace/'),
        ('Robo Weenie', 'http://tappedout.net/mtg-decks/robo-weenie/'),
        ('Savage Ramp', 'http://tappedout.net/mtg-decks/savage-ramp/'),
        ('Secret Plans', 'http://tappedout.net/mtg-decks/24-09-16-secret-plans/'),
        ('Servo Revolt', 'http://tappedout.net/mtg-decks/servo-revolt/'),
        ('Smile At Death', 'http://tappedout.net/mtg-decks/24-09-16-smile-at-death/'),
        ('Sphinx Control', 'http://tappedout.net/mtg-decks/24-09-16-sphinx-control/'),
        ('Spider Spawning', 'http://tappedout.net/mtg-decks/24-09-16-spider-spawning/'),
        ('Storm lords', 'http://tappedout.net/mtg-decks/storm-lords-3/'),
        ('Swarm of Scars', 'http://tappedout.net/mtg-decks/07-08-17-swarm-of-scars/'),
        ('Sweet Vengeance', 'http://tappedout.net/mtg-decks/sweet-vengeance-4/'),
        ('Thermal Detonator', 'http://tappedout.net/mtg-decks/05-01-17-thermal-detonator/'),
        ('Thopter Squad', 'http://tappedout.net/mtg-decks/24-09-16-thopter-squad/'),
        ('Untamed Energy', 'http://tappedout.net/mtg-decks/untamed-energy/'),
        ('Uproar', 'http://tappedout.net/mtg-decks/uproar-2/'),
        ('Warriors!', 'http://tappedout.net/mtg-decks/24-09-16-warriors/'),
        ('Zombie Apocolypse', 'http://tappedout.net/mtg-decks/24-09-16-zombie-apocolypse/'),
    ]


def get_battle_decks_from_tappedout(deck_list_tuple):
    return_cards_list = []
    for deck_tuple in deck_list_tuple:
        deck_name = deck_tuple[0]
        print('\nDeck: ' + deck_name)
        deck_url = deck_tuple[1]
        r = requests.get(deck_url)
        r_soup = BeautifulSoup(r.text, 'html.parser')
        soup_elements = r_soup.findAll('textarea', {'id': 'mtga-textarea'})
        card_list_text = soup_elements[0].text.strip()
        card_list = card_list_text.split('\n')
        for card in card_list:
            card = card.strip()
            quantity = card[:card.find(' ')].strip()
            card_name = card[card.find(' '):card.find(' (')].strip()
            line_list = [card_name, deck_name, quantity]
            return_cards_list.append('\t'.join(line_list))
    return return_cards_list


def main():
    battle_deck_list_tuple = get_battle_decks()
    cards_list = get_battle_decks_from_tappedout(deck_list_tuple=battle_deck_list_tuple)
    import pprint
    pprint.pprint(cards_list)
    filename = 'battle_decks.tsv'
    with open(file=filename, mode='w') as f:
        print('Writing out file: ' + filename)
        f.write('\n'.join(cards_list))


main()
