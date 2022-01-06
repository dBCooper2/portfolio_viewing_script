# This is the main Program for connecting to the TDA API
import functions as f

curr_client = f.login()
print(f.get_all_positions(curr_client))