#!/usr/bin/python
#
# get_vps_slice_types
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# We have several types of Servers available for use with VPS Hosting. You can get
# a list of the types available and  there cost per slice/unit by making a call to
# this function
#
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
result = client.service.get_vps_slice_types()
print result