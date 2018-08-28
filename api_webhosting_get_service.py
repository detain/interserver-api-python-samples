#!/usr/bin/python
#
# api_webhosting_get_service
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# This Function Applies to the Webhosting services.
# Gets service info for the given ID in the given Module.   An example of this
# would be in the "vps" module have order id
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param id int 
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_webhosting_get_service()
print result
