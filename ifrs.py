class Output(object):

	def __init__(self):
		self.startContract = '01/10/2018'
		self.endContract = '02/10/2019'
		self.handsetPrice = 32242.99
		self.handsetDiscount = 4672.90
		self.packagePrice = 599.00
		self.duration = 12

		# Range bill cycle
		self.startBill, self.endBill, self.codeCycle = BillCycle.main(self, self.startContract)
		
		# A formula what we used many times.

		# Contract Trans Price
		self.discountAndHandset = round(self.handsetPrice-self.handsetDiscount,2)
		self.totalPackagePrice = round(self.packagePrice*self.duration,2)
		self.sumTransAllPrice = self.handsetPrice-self.handsetDiscount+self.totalPackagePrice # total trans price
		self.sumTransPrice = self.handsetPrice+self.totalPackagePrice # total ssp

		# Allocating Price
		self.percentHandset = round((self.handsetPrice / self.sumTransPrice)*100,2)
		self.percentPackage = round((self.totalPackagePrice / self.sumTransPrice)*100,2)
		self.sumPercentComp = round(self.percentHandset+self.percentPackage,2)
		self.revenueCompHand = round((self.percentHandset * self.sumTransAllPrice)/100,2)
		self.revenueCompPack = round((self.percentPackage * self.sumTransAllPrice)/100,2)
		self.sumRevenueComp = round(self.revenueCompHand+self.revenueCompPack,2)
	def scenarioInput(self): 
		print('**** SCENARIO INPUTS ****')
		print('Transaction Price: %s | %s | %s' % (self.handsetPrice, self.handsetDiscount, self.packagePrice))
		print('Standalone Selling Price [SSP]: %s | %s' % (self.handsetPrice, self.packagePrice))
		print('Duration Contract: %s' % self.duration)
		print('Contract Start: %s' % self.startContract)
		print('Contract End: %s' % self.endContract)
		print('Bill Cycle %s to %s' % (self.startBill, self.endBill))

	def contractTransactionPrice(self): 
		print('**** CONTRACT TRANSACTION PRICE and STANDALONE SELLING PRICE ****')
		print('Transaction Price: %s | %s | %s | \033[4m%s\033[0m' % (self.handsetPrice, self.handsetDiscount*-1, self.totalPackagePrice, round(self.sumTransAllPrice, 2)))
		print('Total Contract SPP %s | %s | \033[4m%s\033[0m' % (self.handsetPrice, self.totalPackagePrice, round(self.sumTransPrice, 2)))
		
	def allocating(self):
		print('**** ALLOCATING REVENUE TO COMPONENTS ****')	
		print('Total Transaction Price %s | %s | %s | \033[4m%s\033[0m' % (self.handsetPrice, self.handsetDiscount*-1, self.totalPackagePrice, round(self.sumTransAllPrice, 2)))
		print('Total Standalone Selling Price [SPP]: %s | %s | \033[4m%s\033[0m' % (self.handsetPrice, self.totalPackagePrice, round(self.sumTransPrice, 2)))
		print('Percentage-per Components: %s%% | %s%% | \033[4m%s%%\033[0m' % (self.percentHandset, self.percentPackage, self.sumPercentComp))
		print('Revenue Allocated to Component: %s | %s | \033[4m%s\033[0m' % (self.revenueCompHand, self.revenueCompPack, self.sumRevenueComp)) # round((a * b) / 100,2)

class BaseFormula(object):

	def checkMonth(self ,month, year):
		if month in (1, 3, 5, 7, 8, 10, 12):
			return 31
		elif month in (4, 6, 9, 11):
			return 30
		else:
	   		if month == 2 and self.checkYear(year) == 366:
	   			return 29
	   		return 28

	def checkYear(self, year):
		if year%4 != 0:
  			return 365
		elif year%100 != 0:
  			return 366
		elif year%400 != 0:
  			return 365
		else:
  			return 366

	def cuttingString(self, a):
  		return int(a[0:2]), int(a[3:5]), int(a[6:10]) # a, b, c

class BillCycle(object):
	
	def main(self, date):
		day, month, year = BaseFormula.cuttingString(self, date)
		startBill, endBill = 0, 0
		bc_name = ''

		if day:
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
			elif day in range(28, BaseFormula.checkMonth(self, month, year)+1): # 28, end_month
				startBill = 28
				bc_name = 'BC17'
			elif day in range(1, 5):
				startBill = 1
				endBill = BaseFormula.checkMonth(self, month, year)
				bc_name = 'BC18'
			if bc_name in ('BC11', 'BC12', 'BC13', 'BC14', 'BC15', 'BC16', 'BC17'):
				endBill = startBill-1
		return startBill, endBill, bc_name


a = Output()
print('')
a.scenarioInput()
print('')
a.contractTransactionPrice()
print('')
a.allocating()
print('')




# === not used ===
	#def basicInform(self):
	#	day_start, month_start, year_start = BaseFormula.cuttingString(self, self.startContract)
	#	day_end, month_end, year_end = BaseFormula.cuttingString(self, self.startContract)
	#	daysInMonth = BaseFormula.checkMonth(self, month_start, year_start)
	#	checkCycle = BillCycle.main(self, self.startContract)
	#	print('Contract Start: %s' % self.startContract)
	#	print('Contract End: %s' % self.endContract)
	#	print('Duration Contract: %s' % self.duration)
