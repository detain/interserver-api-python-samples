#!/usr/bin/python
#
# api_viewTicket
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# View/Retrieve information about the given ticketID.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param ticketID string the id of the ticket to retrieve. you can use [getTicketList](#getticketlist) to get a list of your tickets
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_viewTicket()
print result
