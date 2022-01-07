# portfolio_viewing_script
A Script to view Stock Positions on TDAmeritrade through the Terminal

Big Shoutouts to Alex Golec for writing the tda-api and its docs, I wouldn't be able to make this without him and the project's contributors

Some Notes: 
	- This is for use with Firefox, so the program uses geckodriver. For Chrome Users there is a chromedriver executable you can use instead, just make the necessary adjustments in the functions.py code and it'll work with another browser
	
	- I installed the webdriver on my mac using Homebrew's 'brew install geckodriver' command, then got the path for the geckodriver using 'which geckodriver'. You can use this with bash to achieve the same results, unfortunately I don't know if the cmd or zsh terminals are similar to this.
	
	- Your Token File will expire after a certain amount of inactivity, so you may need to do a manual login from time to time

How to Use:
	- Create an App through the TDAmeritrade API website
	
	- Create a File named 'config.py' with the following variables:
		- 'api_key': this is the API key you receive for your TD App
		- 'token_path': this can simply be 'token' unless you want to store it in a different folder, this is the file path to the auth token
		- 'redirect_uri': this is the redirect URI you entered into the form when you created your app on TDAmeritrade's API, 'https://localhost' worked for me
		- 'td_acct_num': This is the account number to your TD Ameritrade Account
		
	- Edit the executable_path variable in function.py's login() function to match your webdriver install location. If you are using Chrome and chromedriver, simply change the 'Firefox' text to 'Chrome' and then make sure the executable_path variable is the correct location for the chromedriver install
	
Building the Shellscript to run the File(in Bash):
	- Create a file with the .sh extension
	
	- At the top of the file, add the text '#1/bin/bash' to make the shellscript executable
	
	- Have the Script navigate to the folder that build.py is contained in and then add the command 'python3 build.py'
		- EX:
			cd
			cd path/to/python/files
			python3 build.py
	
	- Now that the script file is complete, navigate to the folder the script is saved in within the terminal and enter the command 'chmod u+x name_of_your_script.sh'
	
	- And now you have an executable script, simply navigate to the folder the script is in and enter the command './name_of_your_script.sh' to view your stock positions!