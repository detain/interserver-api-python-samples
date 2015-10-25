#!/usr/bin/python
#
# api_get_dns_records
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Gets the DNS records associated with given Domain ID
#
# @param sid string the *Session ID* you get from the [api_login](#api_login) call
# @param domain_id int The ID of the domain in question.
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
	
result = client.service.api_get_dns_records()
print result