#!/usr/bin/python
#
# api_ssl_get_client_invoices
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# This Function Applies to the SSL Certificates services.
# Gets a list of all the invoices.
#
# @param sid string the *Session ID* you get from the [login](#login) call
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_ssl_get_client_invoices()
print result
