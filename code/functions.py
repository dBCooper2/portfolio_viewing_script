# This will contain Function Definitions for Connecting to the TDA API
import config as cf
import json
import httpx
from tda import auth, client

##########################################################################################
# Connect to the API and Login with a Token or create the Token
##########################################################################################
def login():
	try:
		c = auth.client_from_token_file(cf.token_path, cf.api_key)
	except FileNotFoundError:
		from selenium import webdriver
		with webdriver.Firefox(executable_path = r'/opt/homebrew/bin/geckodriver') as driver:
			c = auth.client_from_login_flow(driver, cf.api_key, cf.redirect_uri, cf.token_path)
	
	return c

##########################################################################################


##########################################################################################
# Return all the Positions from an account as a String to Print in the Terminal
def get_all_positions(c):
	# This line doesn't work
	r = c.get_account(cf.td_acct_num, fields=c.Account.Fields.POSITIONS)
	data = r.json()
		
	return to_string(data)
	

# Helper Method to Output the JSON as a String
def to_string(obj):
	pass	
##########################################################################################
