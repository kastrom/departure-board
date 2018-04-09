# Train and bus times ticker for 64x32 LED matrix
# Kris Fields, 2018

import requests, math
from datetime import datetime

app_id = 'a71361cd'
app_key = '4cd17c34a4cee06842c404f5f435460a'
canary_wharf = '930GCAW'
green_man = '490011285N'

url = 'https://api.tfl.gov.uk/StopPoint/' + green_man + '/arrivals'
params = {'app_id': app_id, 'app_key': app_key}

r = requests.get(url, params=params)

boats = r.json()

sorted_boats = []

for b in boats:
    sorted_boats.append({'boat': b[u'lineName'], 'arrival': b[u'timeToStation']})

sorted_boats = sorted(sorted_boats, key=lambda k: k['arrival'])

for boat in sorted_boats:
    print("%s in %s mins" % (boat['boat'],  math.floor(boat['arrival']/60)))
