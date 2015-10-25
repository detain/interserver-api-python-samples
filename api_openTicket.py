#!/usr/bin/python
#
# api_openTicket
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# This command creates a new ticket in our system.  
#
# @param sid string the *Session ID* you get from the [api_login](#api_login) call
# @param user_email string 
# @param user_ip string 
# @param subject string 
# @param product string 
# @param body string 
# @param box_auth_value string 
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