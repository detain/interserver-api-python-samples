#!/usr/bin/python
#
# get_vps_locations_array
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Use this function to get a list of the Locations available for ordering. The id
# field in the return value is also needed to pass to the buy_vps functions.
#
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
	
result = client.service.get_vps_locations_array()
print result