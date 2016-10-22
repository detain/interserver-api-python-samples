#!/usr/bin/python
#
# api_login
#   scripted in 2015 by detain@interserver.net for the MyAdmin API
#
# This function creates a session in our system which you will need to pass to
# most functions for authentication.
#
# @param username string the username (email address) you signed up with.
# @param password string the password you use to login to the web account, or alternatively the API key.
#
from suds.client import Client
client = Client("https://my.interserver.net/api.php?wsdl")
#print client ## shows detailed client info
  
result = client.service.api_login()
print result
