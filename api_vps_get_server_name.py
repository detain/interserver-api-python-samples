#!/usr/bin/python
#
# api_vps_get_server_name
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Get the name of the vps master/host server your giving the id for
#
# @param sid string the *Session ID* you get from the [login](#login) call
# @param id int id of the vps master
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
sid = client.service.api_login(argv[1], argv[2])
if (sid == '')
	die("Got a blank session")
print "Got Session ID "+sid+"\n"
  
result = client.service.api_vps_get_server_name()
print result
