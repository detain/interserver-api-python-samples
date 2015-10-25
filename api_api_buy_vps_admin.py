#!/usr/bin/python
#
# api_api_buy_vps_admin
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Purchase a VPS (admins only).   Returns a comma seperated list of invoices if
# any need paid.  Same as client function but allows specifying which server to
# install to if there are resources available on the specified server.
#
# @param sid string the *Session ID* you get from the [api_login](#api_login) call
# @param os string 
# @param slices int 
# @param platform string 
# @param controlpanel string 
# @param period int 
# @param location int 
# @param version int 
# @param hostname string 
# @param coupon string 
# @param rootpass string 
# @param server int 
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
	
result = client.service.api_api_buy_vps_admin()
print result