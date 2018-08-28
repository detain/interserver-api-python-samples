#!/usr/bin/python
#
# api_openTicket
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# This command creates a new ticket in our system.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param user_email string client email address
# @param user_ip string client ip address
# @param subject string subject of the ticket
# @param product string the product/service if any this is in reference to.
# @param body string full content/description for the ticket
# @param box_auth_value string encryption string?
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_openTicket()
print result
