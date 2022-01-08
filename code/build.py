# This is the main Program for connecting to the TDA API
import functions as f

cin = input('do you want to see your stocks? \ny/n:')
if cin == 'y' or cin == 'Y' or cin == 'yes' or cin == 'Yes' or cin == 'YES':
	curr_client = f.login()
	print(f.get_all_positions(curr_client))
elif cin == 'n' or cin == 'N' or cin == 'no' or cin == 'No' or cin == 'NO':
	print('Ok! Just run ./stonks.sh from the root folder to view them!\n')
	exit()
else:
	print("You can't answer a simple yes/no answer, you shouldn't be trading stocks!")
	exit()

