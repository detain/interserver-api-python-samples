#!/usr/bin/python
#
# api_getTicketList
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Returns a list of any tickets in the system.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param page int page number of tickets to list
# @param limit int how many tickets to show per page
# @param status string null for no status limit or limit to a specific status
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
