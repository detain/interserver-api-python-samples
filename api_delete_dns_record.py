#!/usr/bin/python
#
# api_delete_dns_record
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Deletes a single DNS record
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param domain_id int The ID of the domain in question.
# @param record_id int The ID of the domains record to remove.
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_delete_dns_record()
print result
