class Output(object):

	def __init__(self):
		self.startContract = '09/10/2017'
		self.endContract = '08/10/2018'
		self.handsetPrice = 32242.99
		self.handsetDiscount = 4672.90
		self.packagePrice = 599.00
		self.duration = 12
		self.bill_cycle = BillCycle() # inhert class
		self.base_formula = BaseFormula()
		

		# Range bill cycle
		self.startBill, self.endBill, self.codeCycle = self.bill_cycle.main(self.startContract)
		
		# A formula, Group by functions name.

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

		# Contract Asset
		self.sumImmidateHandAndDisc = round(self.handsetPrice + self.handsetDiscount*-1, 2) # sum of handset and discount handset
		self.diffImmidateCashAndRev = round(self.revenueCompHand - self.handsetPrice, 2)
		self.sumImmidateContAsset = round(self.diffImmidateCashAndRev + self.handsetDiscount, 2)
		self.revenueCompPackPerMonth = round(self.revenueCompPack / self.duration, 2)
		self.diffRevenueCompPackPerMonth = round(self.revenueCompPackPerMonth - self.packagePrice, 2)

	def scenarioInput(self): 
		print('**** SCENARIO INPUTS ****')
		#print('Transaction Price | %s | %s | %s' % (self.handsetPrice, self.handsetDiscount, self.packagePrice))
		#print('Standalone Selling Price [SSP] | %s | %s' % (self.handsetPrice, selfx.packagePrice))
		print('Duration Contract: %s' % self.duration)
		print('Contract Start: %s' % self.startContract)
		print('Contract End: %s' % self.endContract)
		print('Bill Cycle: %s to %s' % (self.startBill, self.endBill))

	def contractTransactionPrice(self): 
		print('**** CONTRACT TRANSACTION PRICE and STANDALONE SELLING PRICE ****')
		print('Transaction Price: %s | %s | %s | [%s]' % (self.handsetPrice, self.handsetDiscount*-1, self.totalPackagePrice, round(self.sumTransAllPrice, 2)))
		print('Total Contract SPP: %s | %s | [%s]' % (self.handsetPrice, self.totalPackagePrice, round(self.sumTransPrice, 2)))
		
	def allocating(self):
		print('**** ALLOCATING REVENUE TO COMPONENTS ****')	
		print('Total Transaction Price: %s | %s | %s | [%s]' % (self.handsetPrice, self.handsetDiscount*-1, self.totalPackagePrice, round(self.sumTransAllPrice, 2)))
		print('Total Standalone Selling Price: [SPP]: %s | %s | [%s]' % (self.handsetPrice, self.totalPackagePrice, round(self.sumTransPrice, 2)))
		print('Percentage-per Components: %s%% | %s%% | [%s%%]' % (self.percentHandset, self.percentPackage, self.sumPercentComp))
		print('Revenue Allocated to Component: %s | %s | [%s]' % (self.revenueCompHand, self.revenueCompPack, self.sumRevenueComp)) # round((a * b) / 100,2)

	def calculateContractAsset(self):
		print('**** CALCULATING THE CONTRACT ASSET - Immediate and Ongoing Events ****')
		print('Total Cashflow: %s | %s | %s | [%s]' % (self.handsetPrice, self.handsetDiscount*-1, self.totalPackagePrice, round(self.sumTransAllPrice, 2)))
		print('Revenue Allocated to Component: %s | %s | [%s]' % (self.revenueCompHand, self.revenueCompPack, self.sumRevenueComp))
		print('Immidate Cashflow: %s | %s | [%s]' % (self.handsetPrice, self.handsetDiscount*-1, self.sumImmidateHandAndDisc))
		print('Immediate Revenue: %s | [%s]' % (self.revenueCompHand,  self.revenueCompHand))
		print('Immediate Contract Asset: %s | %s | [%s]' % (self.diffImmidateCashAndRev, self.handsetDiscount, self.sumImmidateContAsset))
		print('Monthly Cashflow: %s | [%s]' % (self.packagePrice, self.packagePrice))
		print('Monthly Revenue: %s | [%s]' % (self.revenueCompPackPerMonth, self.revenueCompPackPerMonth))
		print('Monthly Contract Asset: %s | [%s]' % (self.diffRevenueCompPackPerMonth, self.diffRevenueCompPackPerMonth))

	def genEventBill(self):
		period = 1
		money = 100000
		revenue = 30000
		diff = 1
		count = 1
		listDate = []
		tmp = ''
		
		startDay, startMonth, startYear = self.base_formula.cuttingString(self.startContract) # start contract date
		endDay, endMonth, endYear = self.base_formula.cuttingString(self.endContract) # end contract date
		startBill, endBill, bc_name = self.bill_cycle.main(self.startContract) # bill cycle infrom

		
		print('%-10s%-12s%-20s%-16s%-11s%-15s' % ('PERIOD', 'EVENT DATE', 'BUSINESS EVENT' ,'CASH FLOW', 'REVENUE', 'DELTA')) # %-10i : '10' is indent space, 'i' is data type
		
		while period != self.duration+1:

			if startMonth == 13:
				startMonth = 1
				startYear+=1
						
			accured_value = self.bill_cycle.calculateAccured(endBill, startDay, startMonth, startYear, self.packagePrice)

			##actual
			nowFullDate = self.base_formula.combineToFullDate(startDay, startMonth, startYear)
			listDate.append(nowFullDate)

			print(listDate)

			if count > 1:
				tmp = listDate[0], listDate[1]
				listDate.pop(0)	
			
			if period >= 12:
				accured_value = 0
			
			#
			#if tmp:
			#	convert_tmp = list(tmp)
			#	actual_value = self.bill_cycle.calculateActual(endBill, convert_tmp[0], convert_tmp[1], self.packagePrice)

			if count == 1:
				actual_value = 0
			actual_value = 10
			print('T%-9s%-s/%-s/%-11s%-19s%-12s%-13s%-10s' % (period, startDay, startMonth, startYear, 'DPR_TRANS', actual_value, revenue, diff)) # actual : 
			print('T%-9s%-s/%-s/%-11s%-19s%-12s%-13s%-10s' % (period, startDay, startMonth, startYear, 'DPR_TRACC', accured_value, revenue, diff)) # acclue : (daysInMonth-nowDay + 1)/lastMonthDay 
			print('T%-9s%-s/%-s/%-8s%-22s%-12s%-13s%-10s' % (period, startDay, startMonth, startYear, 'DPR_TRACCREV', money, revenue, diff)) # reverse-acclue : acclue in lastmonth with negative value 
			print('------------------------------------------------------------------------------')

			if period == self.duration and startDay < endDay: # if period equal duration and startContact is less than endDay
				startMonth-=1
				startDay=endDay
				period-=1

			if period == 1 and startDay != endBill: # if first period by startContract not equal endBill(pay date)
				startDay = endBill
				period = 0


			period+=1
			startMonth+=1
			count+=1
		
			
	
		print("Total : %i" % int(money-1))


	def showReport(self):
		a = Output()
		print('')
		a.scenarioInput()
		print('')
		a.contractTransactionPrice()
		print('')
		a.allocating()
		print('')
		a.calculateContractAsset()
		print('')
		a.genEventBill()





class BaseFormula(object):

	def cuttingString(self, a):
  		return int(a[0:2]), int(a[3:5]), int(a[6:10]) # a, b, c
	
	def combineToFullDate(self, a, b, c):
  		a = str(a)
  		b = str(b)
  		c = str(c)

  		if len(a) == 1:
  			a = '0'+str(a)
  		if len(b) == 1:
  			b = '0'+str(b)
  		return a + '/' + b + '/' + c


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
	   		if month == 2:
	   			a = self.checkYear(year)
	   			if month == 2 and a == 366:
	   				return 29
	   			return 28

	def distanceDate(self, day1, month1, year1, day2, month2, year2):
	  count = 0
	  while True:
	    if day1 == day2 and month1 == month2 and year1 == year2:
	      	return count
	    if self.checkMonth(month1, year1) == day1:
	      	day1=1
	      	month1+=1
	      	count+=1
	    if month1 == 13:
	    	month1=1
	    	year1+=1

	    	day1+=1
	    	count+=1


class BillCycle(object):

	def __init__(self):
		self.base_formula = BaseFormula()

	def calculateAccured(self, bill_day, day, month, year, package_price):
		#accrued : (daysInMonth-nowDay + 1)/daysInMonth * package_price
		daysInMonth = int(self.base_formula.checkMonth(month, year))
		if day != bill_day:
			accured = (round(float(daysInMonth-day+1)/daysInMonth*package_price,2))
		else:
			accured = (round(float(daysInMonth-day)/daysInMonth*package_price,2))
		return accured

	def calculateActual(self, bill_day, lastDate, nowDate ,package_price):
		start_day, start_month, start_year = self.base_formula.cuttingString(lastDate)
		now_day, now_month, now_year = self.base_formula.cuttingString(nowDate)
		daysInLastMonth = self.base_formula.checkMonth(start_month, start_year) # total days in last month
		range_date = self.base_formula.distanceDate(start_day, start_month, start_year, now_day, now_month, now_year)
		actual = float((round(range_date+1,2))/daysInLastMonth)*package_price
		return actual

	
		
	def main(self, date):
		day, month, year = self.base_formula.cuttingString(date)
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
			elif day in range(28, self.base_formula.checkMonth(month, year)+1): # 28, end_month
				startBill = 28
				bc_name = 'BC17'
			elif day in range(1, 6):
				startBill = 1
				endBill = self.base_formula.checkMonth(month, year)
				bc_name = 'BC18'
			if bc_name in ('BC11', 'BC12', 'BC13', 'BC14', 'BC15', 'BC16', 'BC17'):
				endBill = startBill-1
		return startBill, endBill, bc_name



a = Output()

a.showReport()


