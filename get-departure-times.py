# Train and bus times ticker for 64x32 LED matrix
# Kris Fields, 2018

import requests, math
from datetime import datetime

class DepartureTimes:

    def getDepartureTimes(self):
        
        app_id = 'a71361cd'
        app_key = '4cd17c34a4cee06842c404f5f435460a'
        nre_token = '9a744b64-fd64-4103-b835-e136f7eefd90'

        wandsworth_riverside = '930GWRQ'
        canary_wharf = '930GCAW'
        green_man = '490011285N'

        url = 'https://api.tfl.gov.uk/StopPoint/' + green_man + '/arrivals'
        params = {'app_id': app_id, 'app_key': app_key}

        r = requests.get(url, params=params)

        boats = r.json()

        sorted_departures = []

        for b in boats:
            sorted_departures.append({'departure': b[u'lineName'], 'destination': b[u'destinationName'], 'arrival': b[u'timeToStation']})

        sorted_departures = sorted(sorted_departures, key=lambda k: k['arrival'])

        print(boats[0]['stationName'])

        for departure in sorted_departures:
            print("%s to %s in %s mins" % (departure['departure'], departure['destination'],  math.floor(departure['arrival']/60)))

def main():
    foo = DepartureTimes()
    foo.getDepartureTimes()

if __name__ == "__main__":
    main()
