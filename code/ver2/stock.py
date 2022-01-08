# This Class implements a Nested Dictionary to represent a stock
# 	- Each Dictionary follows this convention:
#		example_stock = {'symbol': self.symbol,
#						 'vals': {dict with all the info}}

# Key:
# - symbol: stock ticker symbol
# - pps: Price Per Share
# - ns: Number of Shares
# - tv: Total Value of Shares
# - pp: Purchase Price of Shares
# - pla: P/L Amount for the Day
# - plp: P/L Percentage for the Day
class Stock:
	def __init__(symbol, pps, ns, tv, pp, pla, plp):
		self.symbol = symbol
		self.pps = pps
		self.ns = ns 
		self.tv = tv 
		self.pp = pp 
		self.pla = pla 
		self.plp = plp
		self.struct = build_dict()
	
	# Configure the Dictionary for Sorting the Stocks in the Main Program 
	def build_dict():
		struct = {
				'symbol':self.symbol,
				'vals':
					{ 'pps' : self.pps
					  'ns'  : self.ns
					  'tv'  : self.tv
					  'pp'  : self.pp
					  'pla' : self.pla
					  'plp' : self.plp
					}
				}
		return struct
	
	# Public Getter to Access the Dictionary in the Main Program
	def get_dict():
		return self.struct
	
	# Private Getters for the individual Values of the Stocks
	def __get_symbol():
		return self.symbol
	
	def __get_pps():
		return self.pps
	
	def __get_ns():
		return self.ns
		
	def __get_tv():
		return self.tv
	
	def __get_pp():
		return self.pp
	
	def __get_pla():
		return self.pla
	
	def __get_plp():
		return self.plp
	
	# Private Setters for the individual Values of the Stocks
	def __set_symbol(symbol):
		self.symbol = symbol
	
	def __set_pps(pps):
		self.pps = pps
	
	def __set_ns(ns):
		self.ns = ns
	
	def __set_tv(tv):
		self.tv = tv
	
	def __set_pp(pp):
		self.pp = pp
	
	def __set_pla(pla):
		self.pla = pla
	
	def __set_plp(plp):
		self.plp = plp
