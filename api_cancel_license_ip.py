#!/usr/bin/python
#
# api_cancel_license_ip
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Cancel a License by IP and Type.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param ip string IP Address to cancel
# @param type int Package ID. use [get_license_types](#get-license-types) to get a list of possible types.
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_cancel_license_ip()
print result
