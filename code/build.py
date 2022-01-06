# This is the main Program for connecting to the TDA API
from tda import auth, client
import json

import config as cf
import functions as f

# Main Program:
"""
try:
	c = auth.client_from_token_file(cf.token_path, cf.api_key)
except FileNotFoundError:
	from selenium import webdriver
	with webdriver.Firefox(executable_path = r'/opt/homebrew/bin/geckodriver') as driver:
		c = auth.client_from_login_flow(driver, cf.api_key, cf.redirect_uri, cf.token_path)
"""

curr_client = f.login()
print(f.get_all_positions(curr_client))