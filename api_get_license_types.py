#!/usr/bin/python
#
# api_get_license_types
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Get a license of the various license types.
#
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
result = client.service.api_get_license_types()
print result
