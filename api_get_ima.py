#!/usr/bin/python
#
# api_get_ima
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Returns the IMA value.  This function tells you that I'm a client, or I'm a
# admin. This is almost always going to return client, Adminsitrators will get an
# admin response.
#
# @param sid string the *Session ID* you get from the [login](#login) call
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_get_ima()
print result
