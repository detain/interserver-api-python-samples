#!/usr/bin/python
#
# api_change_license_ip
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Change the IP on an active license.
#
# @param sid string the *Session ID* you get from the [api_login](#api_login) call
# @param oldip string the old ip address
# @param newip string the new ip address
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
  die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_change_license_ip()
print result