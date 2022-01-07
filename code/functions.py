# This will contain Function Definitions for Connecting to the TDA API

# Imports from my Own Files
import config as cf

# Imports from Other Libraries
from tda import auth, client
import json

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
	

# Helper Method to Output the JSON Dictionary as a Readable String in the terminal
# 	The Dictionary will be printed as a table like this:
#
# (Name)	(Quantity)	(Price Bought)	(Current Price)	(Total Value)	(P/L %)
# 	Val1		Val2		Val3			Val4				Val5	   Val6
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
					for k in obj[i][j]:
						print(k) # Comment this out after
						print('\n\n') # Comment this out after
						
				elif j == 'projectedBalances':
					print('Accessing proj.Balances')
				else:
					continue

##########################################################################################
