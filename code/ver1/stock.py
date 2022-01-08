class Stock:
	def __init__(symbol, pps, ns, tv, pp, pla, plp):
		self.symbol = symbol # Ticker Symbol
		self.pps = pps # Price Per Share
		self.ns = ns # Number of Shares
		self.tv = tv # Total Value of Shares
		self.pp = pp # Purchase Price of the Shares
		self.pla = pla # P/L Amount for the Day
		self.plp = plp # P/L Percentage for the Day
		
	def get_stock_as_string()