from requests import get
import csv

name_price_list = []
with open('artifact_hero_names.csv', 'r') as f:
    hero_names = list(csv.reader(f))[0]
for start in [0,100,200]:
    url = 'https://steamcommunity.com/market/search/render?appid=583950&norender=1&start={}&count={}'.format(start, start+100)
    listings_json = get(url).json()['results']
    for listing in listings_json:
        name_price_list.append((listing['name'], listing['sell_price']))

# 3 of each non-hero card
# 1 of each hero
set_price = 0
for card in name_price_list:
    if card[0] in hero_names:
        set_price = set_price + card[1]
    else:
        set_price = set_price + 3*card[1]

print(set_price/100)
