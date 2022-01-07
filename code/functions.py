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
	final_table_str = ''
	if type(obj) != dict:
		print('Error! Object passed in was not a dictionary! Exiting...')
		exit()
	else:
		stock_positions = list()
	
		for i in obj.keys(): # Just the securities layer
			#print(i) # Delete Later 
			for j in obj[i].keys():
				
				# Accessing all the Positions in the Account:
				if j == 'positions':
					
					# Converting Each of the Positions to the Table Format
					for k in obj[i][j]:
						print(k)
						print('\n\n\n')
						convert_pos_dict_to_string(k)
						print('\n\n\n')
							
				elif j == 'projectedBalances':
					print('Accessing proj.Balances')
				else:
					continue
	return final_table_str

# Helper Method to Sort through the Position Dictionaries
def convert_pos_dict_to_string(k):
	for i in k.keys():
		if i == 'averagePrice': # The price the shares were bought at
			pass # access the key-value pair
		elif i == 'longQuantity': # The number of Shares owned
			pass # access the key-value pair
		elif i == 'marketValue': # The total value of the Position
			pass # access the key-value pair
		elif i == 'instrument': # Get the name of the Position
			for j in i.keys():
				if j == 'symbol':
					# access the symbol key-value pair
				else:
					continue
			pass
		elif i == 'currentDayProfitLoss': # P/L from the day
			pass # access the key-value pair
		elif i == 'currentDayProfitLossPercentage': # P/l % from the day
			pass # access the key-value pair
		else:
			continue
	
	# now that those are done figure out a good way to return these 
##########################################################################################
