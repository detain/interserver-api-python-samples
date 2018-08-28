#!/usr/bin/python
#
# api_ticketPost
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# This commands adds the content parameter as a response/reply to an existing
# ticket specified by ticketID.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param ticketID string the id of the ticket to add a response to. you can use [getTicketList](#getticketlist) to get a list of your tickets
# @param content string the message to add to the ticket
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_ticketPost()
print result
