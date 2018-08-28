#!/usr/bin/python
#
# api_api_auto_cpanel_login
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Logs into cpanel for the given website id and returns a unique logged-in url. 
# The status will be "ok" if successful, or "error" if there was any problems
# status_text will contain a description of the problem if any.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param id int id of website
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_api_auto_cpanel_login()
print result
