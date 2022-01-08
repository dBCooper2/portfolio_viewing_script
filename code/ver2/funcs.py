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
		with webdriver.Firefox(executable_path = r'/opt/home/bin/geckodriver') as driver:
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
	data = r.json()
	print(data)

# Helper Method to Pass in Position jsons to the __init__() function of stock.py
def convert_positions_to_class():
	pass
