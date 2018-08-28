#!/usr/bin/python
#
# api_buy_license_prepay
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Purchase a License and optionally uses PrePay.  Will return an error if
# use_prepay is true not enough PrePay funds are available.
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param ip string ip address you wish to license some software on
# @param type int the package id of the license type you want. use [get_license_types](#get-license-types) to get a list of possible types.
# @param coupon string an optional coupon
# @param use_prepay bool optional, whether or not to use a prepay, if specified as true will return an error if not enough prepay
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_buy_license_prepay()
print result
