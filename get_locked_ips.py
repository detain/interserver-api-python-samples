#!/usr/bin/python
#
# get_locked_ips
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# This will return a list of all IP addresses used for fraud.   Its probably of no
# real use to anyone, butI use it to block IP addresses and similar things. 
#
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
result = client.service.get_locked_ips()
print result
