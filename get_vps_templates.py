#!/usr/bin/python
#
# get_vps_templates
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# Get the currently available VPS templates for each server type.
#
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
result = client.service.get_vps_templates()
print result
