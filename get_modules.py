#!/usr/bin/python
#
# get_modules
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Returns a list of all the modules available.
#
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
result = client.service.get_modules()
print result
