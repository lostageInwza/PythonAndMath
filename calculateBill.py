class Calculation:
	
	def cuttingString(self, a):
  		return a[0:2], a[3:5], a[6:10]

	def zeroRemover(self, date):
  		day, month, year = self.cuttingString(date)
  		if day.find('0') >= 0 or month.find('0') >= 0:
  			day = day.replace('0', '')
  			month = month.replace('0', '')
  		return int(day), int(month), int(year)

	def billCycle(self, date):
		day, month, year = self.zeroRemover(date)
		startBill, endBill = 0, 0
		bc_name = ''
		if day:
			print(month, self.checkMonth(month, year))
			if day in range(6, 8): # 6, 7
				startBill = 4
				bc_name = 'BC11'
			elif day in range(6, 12): # 8, 11
				startBill = 8
				bc_name = 'BC12'
			elif day in range(12, 17): # 12, 16
				startBill = 12
				bc_name = 'BC13'
			if day in range(17, 20): # 17, 19
				startBill = 16
				bc_name = 'BC14'
			elif day in range(20, 24): # 20, 23
				startBill = 20
				bc_name = 'BC15'
			elif day in range(24, 28): # 24, 27
				startBill = 24
				bc_name = 'BC16'
			elif day in range(28, self.checkMonth(month, year)): # 28, end_month
				startBill = 28
				bc_name = 'BC17'
			elif day in range(1, 5):
				startBill = 1
				endBill = self.checkMonth(month, year)
				bc_name = 'BC18'
		
			if bc_name in ('BC11', 'BC12', 'BC13', 'BC14', 'BC15', 'BC16', 'BC17'):
				endBill = startBill-1
		return startBill, endBill, bc_name

	def checkYear(self, year):
		if year%4 != 0:
  			return 365
		elif year%100 != 0:
  			return 366
		elif year%400 != 0:
  			return 365
		else:
  			return 366
	def checkMonth(self ,month, year):
		if month in (1, 3, 5, 7, 8, 10, 12):
			return 31
		elif month in (4, 6, 9, 11):
			return 30
		else:
	   		if year == 365:
	   			return 28
	   		return 29


c = Calculation()
#c.zeroRemover('19/11/2018')
print(c.billCycle('30/04/2018'))

#print(c.billCycle(18, 12, 2018))