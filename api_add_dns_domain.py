#!/usr/bin/python
#
# api_add_dns_domain
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Adds a new domain into our system.  The status will be "ok" if it added, or
# "error" if there was any problems status_text will contain a description of the
# problem if any.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param domain string domain name to host
# @param ip string ip address to assign it to.
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_add_dns_domain()
print result
