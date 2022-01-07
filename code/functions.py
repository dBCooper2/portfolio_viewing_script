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
	data = r.json() # The JSON is now a dictionary
		
	return to_string(data)
	

# Helper Method to Output the JSON Dictionary as a Readable String
"""
1 - Check to be sure the obj is a dictionary
2 - Loop through the first layer of the dict(securities)
3 - From there the keys of the sub-dict are...
	- type
	- accountId
	- roundTrips
	- isDayTrader
	- isClosingOnlyRestricted
	- positions: We want this
		- Positions sub-dictionaries/arrays...
	- initialBalances
	- currentBalances
	- projectedBalances: We want this
		- ProjectedBalances sub-dictionary... we want both of these
			- cashAvailableForTrading
			- cashAvailableForWithdrawal
"""
def to_string(obj):
	if type(obj) != dict:
		print("Error! Object passed in was not a dictionary! Exiting...")
		exit()
	else:
		for i in obj.keys(): # Just the securities layer
			#print(i) # Delete Later 
			for j in obj[i].keys():
				#print(j) # Delete Later
				if j == 'positions':
					print('Accessing Positions')
				elif j == 'projectedBalances':
					print('Accessing proj.Balances')
				else:
					continue

##########################################################################################
