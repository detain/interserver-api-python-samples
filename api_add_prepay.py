#!/usr/bin/python
#
# api_add_prepay
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Adds a PrePay into the system under the given module.    PrePays are a credit on
# your account by prefilling  your account with funds.   These are stored in a
# PrePay.    PrePay funds can be automatically used as needed or set to only be
# usable by direct action
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param module string the module the prepay is for. use [get_modules](#get_modules) to get a list of modules
# @param amount float the dollar amount of prepay total
# @param automatic_use bool whether or not the prepay will get used automatically by billing system.
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_add_prepay()
print result
