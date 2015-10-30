#!/usr/bin/python
#
# api_update_dns_record
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Updates a single DNS record
#
# @param sid string the *Session ID* you get from the [api_login](#api_login) call
# @param domain_id int The ID of the domain in question.
# @param record_id int The ID of the record to update
# @param name string the hostname being set on the dns record.
# @param content string the value of the dns record, or what its set to.
# @param type string dns record type.
# @param ttl int dns record time to live, or update time.
# @param prio int dns record priority
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
  die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_update_dns_record()
print result