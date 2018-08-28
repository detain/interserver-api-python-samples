#!/usr/bin/python
#
# api_make_payment
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Makes a payment for an invoice on a module.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param module string the module of the service being paid on
# @param invoice int the invoice id you want to make a payment on
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_make_payment()
print result
