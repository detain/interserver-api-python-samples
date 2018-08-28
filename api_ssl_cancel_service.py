#!/usr/bin/python
#
# api_ssl_cancel_service
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# This Function Applies to the SSL Certificates services.
# Cancels a service for the passed module matching the passed id.  Canceling a
# service will also cancel any addons for that service at the same time.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param id int ID / Service ID you wish to cancel
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_ssl_cancel_service()
print result
