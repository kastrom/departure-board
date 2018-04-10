# Train and bus times ticker for 64x32 LED matrix
# Kris Fields, 2018

import os
from nredarwin.webservice import DarwinLdbSession

os.environ["DARWIN_WEBSERVICE_API_KEY"] = "9a744b64-fd64-4103-b835-e136f7eefd90"

# initiate a session
# this depends on the DARWIN_WEBSERVICE_API_KEY environment variable
# The WSDL environment variable also allows for
darwin_session = DarwinLdbSession(wsdl='https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx')

crs_code = 'WNT'
# retrieve departure board
board = darwin_session.get_station_board(crs_code)

# print table header
print("\nNext departures for %s" % (board.location_name))
print("""
-------------------------------------------------------------------------------
|  PLAT  | DEST                                        |   SCHED   |    DUE   |
------------------------------------------------------------------------------- """)

# Loop through services
for service in board.train_services:
    print("| %6s | %43s | %9s | %8s |" %(service.platform or "", service.destination_text, service.std, service.etd))

# Print a footer 
print("-------------------------------------------------------------------------------")
