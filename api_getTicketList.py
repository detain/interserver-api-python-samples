#!/usr/bin/python
#
# api_getTicketList
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Returns a list of any tickets in the system.
#
# @param sid string the *Session ID* you get from the [api_login](#api_login) call
# @param page int 
# @param limit int 
# @param status string 
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
	
result = client.service.api_getTicketList()
print result