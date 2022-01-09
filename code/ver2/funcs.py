# This contains the Main Functions for the Program to keep the Build.py file clean
import config as cf
from tda import auth, client
import json

# Function to Login through Firefox with the TDAmeritrade API and generate an OAuth Token
def ff_login():
	try:
		c = auth.client_from_token_file(cf.token_path, cf.api_key)
	except FileNotFoundError:
		from selenium import webdriver
		with webdriver.Firefox(executable_path = r'/opt/homebrew/bin/geckodriver') as driver:
			c = auth.client_from_login_flow(driver, cf.api_key, cf.redirect_uri, cf.token_path)
			
	return c
	
# Might add functionality for these, we'll see
# def chrome_login():
#	pass
# def safari_login():
#	pass

# Function to call the tda_api's get_account() function
#	Figure out an elegant way to pass the files into the stock.py file!!!
def get_account_positions(c):
	r = c.get_account(cf.td_acct_num, fields=c.Account.Fields.POSITIONS)
	data = r.json() # This is the raw json, the whole shebang
	print(data)
	# Add something here to filter the data into just dict of the stock positions
	positions = filter_positions(data)
	print('\n\n')
	print(positions)
	# Add another method to get just the dict of the current balances
	balances = filter_balances(data)
	print('\n\n')
	print(balances)
	convert_positions_to_class(positions)
	
# Helper Method to take the big raw json and spit out just the positions
def filter_positions(data):
	# Access the data['securities'] layer
		# Access the data['positions'] layer and spit it out
	return data['securitiesAccount']['positions'] # Does this work?

# Helper Method to take the big raw json and spit out just the current balances
def filter_balances(data):
	return data['securitiesAccount']['currentBalances']

# Helper Method to Pass in Position jsons to the __init__() function of stock.py
def convert_positions_to_class(positions):
	pass
	
	
# Sort these Alphabetically
def sort_stocks(stocks):
	pass
