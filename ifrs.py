#support Case1, Case10

#make every number to decimal 2 points

class Output(object):

	def __init__(self):
		self.bill_cycle = BillCycle() # inhert class
		self.base_formula = BaseFormula()
		self.startContract = '15/09/2017'
		self.endContract = '14/09/2018'
		self.handsetPrice = 24766.36
		self.handsetDiscount = -1769.16
		self.specialDiscount = -500.00 # Case 10
		self.packagePrice = 500.00
		
		#bill cycle infrom
		self.bill_from, self.bill_to, self.bc_type = self.bill_cycle.main(self.startContract)
		# duration : calculate from range betwenn
		self.day1, self.month1, self.year1 = self.base_formula.cuttingString(self.startContract) # extract contract start
		self.day2, self.month2, self.year2 = self.base_formula.cuttingString(self.endContract)
		self.duration = self.base_formula.collectTotalMonth(self.month1, self.year1, self.month2, self.year2)

		# Range bill cycle
		self.startBill, self.endBill, self.codeCycle = self.bill_cycle.main(self.startContract)
		
		# A formula, Group by functions name.

		# Contract Trans Price
		self.discountAndHandset = round(self.handsetPrice+self.handsetDiscount,2)
		self.totalPackagePrice = round(self.packagePrice*self.duration,2)
		self.sumTransAllPrice = self.handsetPrice+self.handsetDiscount+self.totalPackagePrice+self.specialDiscount # total trans price
		self.sumTransPrice = self.handsetPrice+self.totalPackagePrice # total ssp

		# Allocating Price
		self.percentHandset = round((self.handsetPrice / self.sumTransPrice)*100,2)
		self.percentPackage = round((self.totalPackagePrice / self.sumTransPrice)*100,2)
		self.sumPercentComp = round(self.percentHandset+self.percentPackage,2)
		self.revenueCompHand = round((self.percentHandset * self.sumTransAllPrice)/100,2)
		self.revenueCompPack = round((self.percentPackage * self.sumTransAllPrice)/100,2)
		self.sumRevenueComp = round(self.revenueCompHand+self.revenueCompPack,2)

		# Contract Asset
		self.sumImmidateHandAndDisc = round(self.handsetPrice + self.handsetDiscount, 2) # sum of handset and discount handset
		self.diffImmidateCashAndRev = round(self.revenueCompHand-self.handsetPrice, 2)
		self.sumImmidateContAsset = round(self.diffImmidateCashAndRev + (self.handsetDiscount*-1) + (self.specialDiscount*-1), 2)
		self.revenueCompPackPerMonth = round(self.revenueCompPack / self.duration, 2)
		self.diffRevenueCompPackPerMonth = round(self.revenueCompPackPerMonth - self.packagePrice, 2)

	def scenarioInput(self):
		print('**** SCENARIO INPUTS ****')
		print('Duration Contract: %s' % self.duration)
		print('Contract Start: %s' % self.startContract)
		print('Contract End: %s' % self.endContract)
		print('Bill Cycle: %s to %s' % (self.startBill, self.endBill))

	def contractTransactionPrice(self):
		print('*** CONTRACT TRANSACTION PRICE and STANDALONE SELLING PRICE ***')
		print('-'*63)	
		print('%-25s%-20s%-20s' % ('Component', 'Transcation Price', 'Total Contract'))
		print('-'*63)
		print('%-36s%-17s%s' % ('Service Plan', self.totalPackagePrice, self.totalPackagePrice))
		print('%-34s%-17s%s' % ('Handset', self.handsetPrice, self.handsetPrice))
		print('%-34s%-24s%s' % ('Normal Discount', self.handsetDiscount, 0))
		if self.specialDiscount != 0:
			print('%-38s%-20s%s' % ('Special Discount', self.specialDiscount, 0))
		print('-'*63)
		print('%-35s%-16s%s' % ('Total', round(self.sumTransAllPrice,2), round(self.sumTransPrice, 2)))
		print('-'*63)

	def allocating(self):
		print('**** ALLOCATING REVENUE TO COMPONENTS ****')
		print('-'*150)
		print('%-21s%-30s%-35s%-30s%-20s' % ('Component', 'Total Transcation Price', 'Total Standard Selling Price', 'Percentage-per Components', 'Revenue Allocated to Component'))
		print('-'*150)
		print('%-38s%-35s%-33s%-s%-30s%s' % ('Service Plan', self.totalPackagePrice, self.totalPackagePrice, self.percentPackage,'%', self.revenueCompPack))
		print('%-36s%-35s%-35s%s%-29s%s' % ('Handset', self.handsetPrice, self.handsetPrice, self.percentHandset, '%', self.revenueCompHand))
		print('%-36s%-40s%-31s%-37s%s' % ('Normal Discount', self.handsetDiscount, 0.00, 0.00, 0.00))
		if self.specialDiscount != 0:
			print('%-40s%-36s%-31s%-37s%s' % ('Special Discount', self.specialDiscount, 0.00, 0.00, 0.00))
		print('-'*150)
		print('%-37s%-34s%-35s%-s%-30s%s' % ('Total', round(self.sumTransAllPrice,2), round(self.sumTransPrice,2), self.sumPercentComp, '%', self.sumRevenueComp))
		print('-'*150)


	def calculateContractAsset(self):
		print('**** CALCULATING THE CONTRACT ASSET - Immediate and Ongoing Events ****')
		print('-'*211)
		print('%-17s%-21s%-35s%-23s%-23s%-30s%-20s%-20s%s' %('Component','Total Cashflow', 'Revenue Allocated to Component', 'Immidate Cashflow', 'Immediate Revenue', 'Immediate Contract Assets', 'Monthly Cashflow', 'Monthly Revenue', 'Monthly Contract Asset'))
		print('-'*211)
		print('%-25s%-35s%-29s%-23s%-31s%-15s%-20s%-20s%s' % ('Service Plan', self.totalPackagePrice, self.revenueCompPack,0 ,0 ,0, self.packagePrice, self.revenueCompPackPerMonth, self.diffRevenueCompPackPerMonth))
		print('%-23s%-36s%-23s%-23s%-31s%-26s%-20s%-20s%s' % ('Handset', self.handsetPrice, self.revenueCompHand, self.handsetPrice, self.revenueCompHand, self.diffImmidateCashAndRev,0 ,0 ,0))
		print('%-24s%-42s%-16s%-30s%-25s%-24s%-22s%-18s%-22s' % ('Normal Discount', self.handsetDiscount, 0, self.handsetDiscount, 0, (self.handsetDiscount)*-1, 0, 0, 0))
		if self.specialDiscount != 0:
			print('%-26s%-39s%-18s%-29s%-30s%-20s%-20s%-19s%-10s' % ('Special Discount', self.specialDiscount, 0, self.specialDiscount,0 ,0 ,0, 0, 0))
		print('-'*211)
		print('%-24s%-36s%-22s%-23s%-30s%-24s%-18s%-25s%s' % ('Total', round(self.sumTransAllPrice,2), self.sumRevenueComp, self.sumImmidateHandAndDisc, self.revenueCompHand, self.sumImmidateContAsset, self.packagePrice, self.revenueCompPackPerMonth, self.diffRevenueCompPackPerMonth))
		print('-'*211)
		
		
		#print('Total Cashflow: %s | %s | %s | [%s]' % (self.handsetPrice, self.handsetDiscount*-1, self.totalPackagePrice, round(self.sumTransAllPrice, 2)))
		#print('Revenue Allocated to Component: %s | %s | [%s]' % (self.revenueCompHand, self.revenueCompPack, self.sumRevenueComp))
		#print('Immidate Cashflow: %s | %s | [%s]' % (self.handsetPrice, self.handsetDiscount*-1, self.sumImmidateHandAndDisc))
		#print('Immediate Revenue: %s | [%s]' % (self.revenueCompHand,  self.revenueCompHand))
		#print('Immediate Contract Asset: %s | %s | [%s]' % (self.diffImmidateCashAndRev, self.handsetDiscount, self.sumImmidateContAsset))
		#print('Monthly Cashflow: %s | [%s]' % (self.packagePrice, self.packagePrice))
		#print('Monthly Revenue: %s | [%s]' % (self.revenueCompPackPerMonth, self.revenueCompPackPerMonth))
		#print('Monthly Contract Asset: %s | [%s]' % (self.diffRevenueCompPackPerMonth, self.diffRevenueCompPackPerMonth))

	def genEventBill(self):
		date_list_actual = []
		trans_list_accured = [] # for use in reverse accured
		period = 1

		package_value = self.packagePrice
		actual_value = 0 # real usage value
		accured_value = 0 # estimate usage value
		reverse_accured_value = 0 # reverse accured value in last month

		rev_actual_value = 0
		rev_accured_value = 0
		rev_reverse_accured_value = 0

		diff_value = 0

		trans_day, trans_month, trans_year = self.base_formula.cuttingString(self.startContract)
		end_trans_day, end_trans_month, end_trans_year = self.base_formula.cuttingString(self.endContract)
		
		print('%-10s%-12s%-20s%-16s%-11s%-15s' % ('PERIOD', 'EVENT DATE', 'BUSINESS EVENT' ,'CASH FLOW', 'REVENUE', 'DELTA')) # %-10i : '10' is indent space, 'i' is data type

		while self.duration+1 != period:

			if trans_month == 13: # change years when month value is over than 12
				trans_month = 1
				trans_year+=1
			
			# ====================================== Accured Value ======================================

			if period != self.duration: # if period is not equal duration, accured value will appear
				accured_value =	self.bill_cycle.calculateAccured(self.bill_to, trans_day, trans_month, trans_year, self.packagePrice)
			
			if period == self.duration: # if period is equal duration, accured value is 0
				accured_value = 0
			
			# ====================================== Actual Value ======================================

			full_trans_date = self.base_formula.combineToFullDate(trans_day, trans_month, trans_year)
			date_list_actual.append(full_trans_date)	

			if len(date_list_actual) == 3:
				date_list_actual.pop(0)
			
			if len(date_list_actual) > 1:
				a, b = self.bill_cycle.calculateActual(self.bill_to, date_list_actual[0], date_list_actual[1], package_value)
				actual_value = round(b, 2)
			
			# ====================================== Reverse accured value ======================================
			trans_list_accured.append(accured_value)
			if trans_day != self.day1 and trans_month != self.month1:
				reverse_accured_value = trans_list_accured[0]*-1
			if period == self.duration:
				reverse_accured_value = trans_list_accured[0]*-1

			print('T%-9s%-s/%-s/%-11s%-19s%-12s%-13s%-10s' % (period, trans_day, trans_month, trans_year, 'DPR_TRANS', actual_value, rev_actual_value, diff_value)) # actual : 
			print('T%-9s%-s/%-s/%-11s%-19s%-12s%-13s%-10s' % (period, trans_day, trans_month, trans_year, 'DPR_TRACC', accured_value, rev_accured_value, diff_value)) # acclue : (daysInMonth-nowDay + 1)/lastMonthDay 
			print('T%-9s%-s/%-s/%-8s%-22s%-12s%-13s%-10s' % (period, trans_day, trans_month, trans_year, 'DPR_TRACCREV', reverse_accured_value, rev_reverse_accured_value, diff_value)) # reverse-acclue : acclue in lastmonth with negative value 
			print('------------------------------------------------------------------------------')

			if period == 1 and trans_day not in (self.bill_to, self.bill_from): # if transaction day not like bill_cycle from or to transction day value is bill_to, if transaction day is bill from, it's okay do nothing whith that (not include BC11 case)
				if self.codeCycle == 'BC11': # if bill cycle code is 'BC11', transaction day will renew to bill from
					trans_day = self.bill_from
				else: 
					trans_day = self.bill_to
				period-=1

			if period == self.duration and trans_day != end_trans_day: # if periopd is equal to duration contract and last payment day is not equal end contract date
				if trans_month == end_trans_month: # if last trasaction month is equal end contract month
					trans_day = end_trans_day
					trans_month-=1
				period-=1

				
			if len(trans_list_accured) == 2:
				trans_list_accured.pop(0)

			#main loop
			period+=1
			trans_month+=1


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
	#	print('')
	#	a.genEventBill()


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

	def collectTotalMonth(self,  month1, year1, month2, year2):
		result_list = []
		while True:
			result_list.append(month1)
			month1+=1
			if month1 == 13:
				month1=1
				year1+=1
			if year1 == year2 and month1 == month2:
				return len(result_list)

		#return result_list


class BillCycle(object):

	def __init__(self):
		self.base_formula = BaseFormula()

	def calculateAccured(self, bill_day, day, month, year, package_price):

		daysInMonth = int(self.base_formula.checkMonth(month, year))
		if day != bill_day:
			accured = (round(float(daysInMonth-day+1)/daysInMonth*package_price,2))
		else:
			accured = (round(float(daysInMonth-day)/daysInMonth*package_price,2))
		return accured

	def calculateActual(self, bill_day, lastDate, nowDate ,package_price):
		start_day, start_month, start_year = self.base_formula.cuttingString(lastDate) # lastmonth date
		now_day, now_month, now_year = self.base_formula.cuttingString(nowDate) # now date
	
		daysInLastMonth = self.base_formula.checkMonth(start_month, start_year) # total days in last month
		range_date = self.base_formula.distanceDate(start_day, start_month, start_year, now_day, now_month, now_year)
		actual_not_full_month = float((round(range_date+1,2))/daysInLastMonth)*package_price # not calculate payment full month
		actual_full_month = float((round(range_date,2))/daysInLastMonth)*package_price # calculate payment full month
		return actual_not_full_month, actual_full_month



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

#b = BaseFormula()
#b.distanceDate(4, 9, 2017, 4, 3, 2018)

#self.startContract = '04/09/2017'
#self.endContract = '04/03/2018'

# ========== not used ==========

"""period = 1
		revenue = '-'
		diff = 1
		count = 1
		listDate = []
		accured_list = []
		actual_tmp = ''
		accured_tmp = ''
		

		startDay, startMonth, startYear = self.base_formula.cuttingString(self.startContract) # start contract date
		endDay, endMonth, endYear = self.base_formula.cuttingString(self.endContract) # end contract date
		startBill, endBill, bc_name = self.bill_cycle.main(self.startContract) # bill cycle infrom
		
		print('%-10s%-12s%-20s%-16s%-11s%-15s' % ('PERIOD', 'EVENT DATE', 'BUSINESS EVENT' ,'CASH FLOW', 'REVENUE', 'DELTA')) # %-10i : '10' is indent space, 'i' is data type
		
		while period != self.duration+1:

			if startMonth == 13:
				startMonth = 1
				startYear+=1


			#create accured value
			accured_value = self.bill_cycle.calculateAccured(endBill, startDay, startMonth, startYear, self.packagePrice)

			#reverse actual
			accured_list.append(accured_value)

			#create actual value
			nowFullDate = self.base_formula.combineToFullDate(startDay, startMonth, startYear)
			listDate.append(nowFullDate)

			
			if count > 1:
				accured_tmp = accured_list[0], accured_list[1]
				actual_tmp = listDate[0], listDate[1]
				listDate.pop(0)
				accured_list.pop(0)
			
			if accured_tmp:
				convert_accured_tmp = list(accured_tmp)
				accured_tmp_value = convert_accured_tmp[0]*-1

			if actual_tmp:
				convert_actual_tmp = list(actual_tmp)
				actual_value_not_full, actual_value_full = self.bill_cycle.calculateActual(endBill, convert_actual_tmp[0], convert_actual_tmp[1], self.packagePrice)

			if period >= self.duration:
				accured_value = 0

			if count == 1:
				actual_value = 0
				accured_tmp_value = 0

			if count != 1:
			  if period == 1:
			    actual_value = round(actual_value_not_full, 2) # if period is 1 thats mean it's not in bill cycle loop, effect of that is : total day will not match
			  else:
				  actual_value = round(actual_value_full, 2)

			if self.base_formula.combineToFullDate(startDay, startMonth, startYear)== self.endContract:
				accured_tmp_value = 0

			print('T%-9s%-s/%-s/%-11s%-19s%-12s%-13s%-10s' % (period, startDay, startMonth, startYear, 'DPR_TRANS', actual_value, revenue, diff)) # actual : 
			print('T%-9s%-s/%-s/%-11s%-19s%-12s%-13s%-10s' % (period, startDay, startMonth, startYear, 'DPR_TRACC', accured_value, revenue, diff)) # acclue : (daysInMonth-nowDay + 1)/lastMonthDay 
			print('T%-9s%-s/%-s/%-8s%-22s%-12s%-13s%-10s' % (period, startDay, startMonth, startYear, 'DPR_TRACCREV', accured_tmp_value, revenue, diff)) # reverse-acclue : acclue in lastmonth with negative value 
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
	
		#print("Total : %i" % int(money-1))"""


		#print('Transaction Price: %s | %s | %s | [%s]' % (self.handsetPrice, self.handsetDiscount*-1, self.totalPackagePrice, round(self.sumTransAllPrice, 2)))
		#print('Total Contract SPP: %s | %s | [%s]' % (self.handsetPrice, self.totalPackagePrice, round(self.sumTransPrice, 2)))
		

		#print('Total Transaction Price: %s | %s | %s | [%s]' % (self.handsetPrice, self.handsetDiscount*-1, self.totalPackagePrice, round(self.sumTransAllPrice, 2)))
		#print('Total Standalone Selling Price: [SPP]: %s | %s | [%s]' % (self.handsetPrice, self.totalPackagePrice, round(self.sumTransPrice, 2)))
		#print('Percentage-per Components: %s%% | %s%% | [%s%%]' % (self.percentHandset, self.percentPackage, self.sumPercentComp))
		#print('Revenue Allocated to Component: %s | %s | [%s]' % (self.revenueCompHand, self.revenueCompPack, self.sumRevenueComp)) # round((a * b) / 100,2)