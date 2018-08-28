#!/usr/bin/python
#
# api_get_prepay_paypal_fill_url
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Gets a PayPal URL to fill a PrePay.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param module string the module the prepay is for. use [get_modules](#get_modules) to get a list of modules
# @param prepay_id int the ID of the PrePay
# @param amount float the amount to pay on the prepay.
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_get_prepay_paypal_fill_url()
print result
