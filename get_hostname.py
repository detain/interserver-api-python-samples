#!/usr/bin/python
#
# get_hostname
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Resolves an IP Address and returns the hostname it points to.
#
# @param ip string 
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
  
result = client.service.get_hostname()
print result
