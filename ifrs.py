# scenario done 1, 9, 10
# BC 18 not support now [contract_start: 1 - 5] # wait for confirm business logic

import datetime

class Output(object):
	

	def __init__(self):
		self.bill_cycle = BillCycle() # inherit class
		self.base_formula = BaseFormula()
		while True:
			print('Start Contract ex: 01/01/2018')
			self.startContract = str(input('> ')) #'15/09/2017'
			print('End Contract ex: 01/01/2018')
			self.endContract = str(input('> ')) #'14/09/2018'
		
			chk_start_day, chk_start_month, chk_start_year = self.base_formula.cuttingString(self.startContract)
			chk_end_day, chk_end_month, chk_end_year = self.base_formula.cuttingString(self.endContract)
		
			startCon = datetime.date(chk_start_year, chk_start_month, chk_start_day)
			endCon = datetime.date(chk_end_year, chk_end_month, chk_end_day)

			if startCon >= endCon or chk_start_day in range(1, 5):
				print("Something wrong, please check you're date input (This time start contract days in BC18 is not support)")
			else:
				break

			#if chk_start_day < chk_end_day and chk_start_month < chk_end_month or chk_start_year > chk_end_year:
			#	print('Something wrong with date contract, please try again :D')
			#else:
			#	break

		handsetInput = str(input('Handset price: '))
		handsetDiscountInput = str(input('Handset discount: '))
		packagePriceInput = str(input('Package price: '))

		freeGoodsPriceInput = str(input('Free goods price: ')) # If this value are more than 0 calculation for Case 9 will active
		specialDiscountInput = str(input('Special Discount: ')) # If this value are more than 0 calculation for Case 10 will active
		
		self.handsetPrice = self.base_formula.addDecimal(handsetInput)
		self.handsetDiscount = self.base_formula.addDecimal(handsetDiscountInput)
		self.packagePrice = self.base_formula.addDecimal(packagePriceInput)

		
		################################ Case 9 ####################################
		if freeGoodsPriceInput == '' or freeGoodsPriceInput == '0': 
			self.freeGoodsPrice = 0
		else:
			self.freeGoodsPrice = self.base_formula.addDecimal(freeGoodsPriceInput)

		################################ Case 10 ####################################
		if specialDiscountInput == '' or specialDiscountInput == '0':
			self.specialDiscount = 0
		else:
			self.specialDiscount = self.base_formula.addDecimal(specialDiscountInput)

		# Case 7, 8 will active if upgradePackagePrice is more than 0
		#self.changePackagePrice = 1 # if value less than default Case downgrade
		#self.changeDate = '22/10/2017'

		# Case 2 will active if terminate_date is not null
		#self.terminateDate = '20/09/2018'

		# Case 9 will active if free goods price more than 0
		#self.freeGoodsPrice = 4320.00
		
		# Case 10 will active if specialDiscount value is more than 0
		#self.specialDiscount = 3200.00

		#bill cycle infrom
		self.bill_from, self.bill_to, self.bc_type = self.bill_cycle.billCycleInform(self.startContract)
		# duration : calculate from range between
		self.day1, self.month1, self.year1 = self.base_formula.cuttingString(self.startContract) # extract contract start
		self.day2, self.month2, self.year2 = self.base_formula.cuttingString(self.endContract)
		self.duration = self.base_formula.collectTotalMonth(self.month1, self.year1, self.month2, self.year2)
		
		# for inherit class
		#Output.duration_contract = self.duration
		#Output.start_contact = self.startContract
		#Output.end_contract = self.endContract
		#Output.package_price = self.packagePrice
		#Output.change_package_price = self.changePackagePrice
		#Output.change_package_date = self.changeDate

		# Range bill cycle
		self.startBill, self.endBill, self.codeCycle = self.bill_cycle.billCycleInform(self.startContract)
		
		# A formula, Group by functions name.

		# Contract Trans Price
		self.discountAndHandset = round(self.handsetPrice+self.handsetDiscount,2) # Handset Discount
		self.totalPackagePrice = round(self.packagePrice*self.duration,2) # Package Price times with duration contract
		self.sumTransAllPrice = self.handsetPrice+self.handsetDiscount+self.totalPackagePrice+self.specialDiscount # Transaction Price
		self.sumTransPrice = self.handsetPrice+self.totalPackagePrice+self.freeGoodsPrice # Total Contract SPP

		# Allocating Price
		self.percentHandset = (self.handsetPrice / self.sumTransPrice)*100 # Percentage per Component (Handset)
		self.percentPackage = (self.totalPackagePrice / self.sumTransPrice)*100 # Percentage per Component (Package)
		self.percentFreeGoods = (self.freeGoodsPrice / self.sumTransPrice)*100 # Percentage per Component (Free Goods) # case 9

		self.sumPercentComp = round(self.percentHandset + self.percentPackage + self.percentFreeGoods,1) # Sum total percentage (must be 100%)
		
		self.revenueCompHand = (self.percentHandset * self.sumTransAllPrice)/100 # Revenue to component (Handset)
		self.revenueCompPack = (self.percentPackage * self.sumTransAllPrice)/100 # Revenue to component (Package)
		self.revenueFreeGoods = (self.percentFreeGoods * self.sumTransAllPrice)/100 # Revenue to component (Free Goods)

		self.sumRevenueComp = round(self.revenueCompHand + self.revenueCompPack + self.revenueFreeGoods,2) # Total Revenue

		# Contract Asset
		self.sumImmidateHandAndDisc = self.handsetPrice + self.handsetDiscount # Sum Immediate Cashflow (Handset and Discount)
		self.sumImmidateRev = self.revenueCompHand+self.revenueFreeGoods
		self.diffImmidateCashAndRev = round(self.revenueCompHand-self.handsetPrice, 2) # Immediate Contract Asset (Handset)
		self.sumImmidateContAsset = self.diffImmidateCashAndRev + (self.handsetDiscount*-1) + (self.specialDiscount*-1) + self.revenueFreeGoods # Sum immediate contract asset
		self.revenueCompPackPerMonth = self.revenueCompPack / self.duration
		self.diffRevenueCompPackPerMonth = self.revenueCompPackPerMonth - self.packagePrice

	def scenarioInput(self):
		print('**** SCENARIO INPUTS ****')
		print('-'*30)
		print('Duration Contract: %s' % self.duration)
		print('Contract Start: %s' % self.startContract)
		print('Contract End: %s' % self.endContract)
		print('Bill Cycle: %s to %s' % (self.startBill, self.endBill))
		print('-'*30)

	def contractTransactionPrice(self):
		print('*** CONTRACT TRANSACTION PRICE and STANDALONE SELLING PRICE ***')
		print('-'*63)	
		print('%-25s%-20s%-20s' % ('Component', 'Transcation Price', 'Total Contract'))
		print('-'*63)
		print('%-36s%-17s%s' % ('Service Plan', self.totalPackagePrice, self.totalPackagePrice))
		print('%-34s%-17s%s' % ('Handset', self.handsetPrice, self.handsetPrice))
		print('%-34s%-24s%s' % ('Normal Discount', self.handsetDiscount, 0))
		if self.specialDiscount != 0: # for case 10
			print('%-35s%-23s%s' % ('Special Discount', self.specialDiscount, 0))
		if self.freeGoodsPrice != 0: # for case 9
			print('%-38s%-16s%-20s' % ('Free Goods Price', 0, self.freeGoodsPrice))
		print('-'*63)
		print('%-35s%-16s%s' % ('Total', round(self.sumTransAllPrice,2), round(self.sumTransPrice, 2)))
		print('-'*63)

	def allocating(self):
		print('**** ALLOCATING REVENUE TO COMPONENTS ****')	
		print('-'*150)
		print('%-21s%-30s%-35s%-30s%-20s' % ('Component', 'Total Transcation Price', 'Total Standard Selling Price', 'Percentage-per Components', 'Revenue Allocated to Component'))
		print('-'*150)
		print('%-38s%-35s%-33s%-s%-28s%s' % ('Service Plan', self.totalPackagePrice, self.totalPackagePrice, round(self.percentPackage,2),'%', round(self.revenueCompPack,2)))
		print('%-36s%-35s%-35s%s%-28s%s' % ('Handset', self.handsetPrice, self.handsetPrice, round(self.percentHandset,2), '%',round(self.revenueCompHand,2)))
		print('%-36s%-40s%-29s%-37s%s' % ('Normal Discount', self.handsetDiscount, 0.00, 0.00, 0.00))
		if self.specialDiscount != 0: # for case 10
			print('%-38s%-36s%-33s%-37s%s' % ('Special Discount', self.specialDiscount, 0.00, 0.00, 0.00))
		if self.freeGoodsPrice != 0: # for case 9
			print(('%-38s%-38s%-28s%s%-29s%-33s') % ('Free goods things',0 ,0 ,round(self.percentFreeGoods,2), '%', round(self.revenueFreeGoods,2)))
		print('-'*150)
		print('%-37s%-34s%-33s%-s%-30s%s' % ('Total', round(self.sumTransAllPrice,2), round(self.sumTransPrice,2), self.sumPercentComp, '%', self.sumRevenueComp))
		print('-'*150)


	def calculateContractAsset(self):
		print('**** CALCULATING THE CONTRACT ASSET - Immediate and Ongoing Events ****')
		print('-'*211)
		print('%-20s%-25s%-35s%-23s%-23s%-30s%-20s%-20s%s' %('Component','Total Cashflow', 'Revenue Allocated to Component', 'Immidate Cashflow', 'Immediate Revenue', 'Immediate Contract Assets', 'Monthly Cashflow', 'Monthly Revenue', 'Monthly Contract Asset'))
		print('-'*211)
		print('%-28s%-35s%-25s%-21s%-30s%-22s%-22s%-19s%-10s' % ('Service Plan', self.totalPackagePrice, round(self.revenueCompPack,2),0 ,0 ,0, self.packagePrice, round(self.revenueCompPackPerMonth,2), round(self.diffRevenueCompPackPerMonth,2)))
		print('%-28s%-35s%-25s%-21s%-30s%-22s%-22s%-19s%-10s' % ('Handset', self.handsetPrice, round(self.revenueCompHand,2), round(self.handsetPrice,2), round(self.revenueCompHand,2), self.diffImmidateCashAndRev,0 ,0 ,0))
		print('%-28s%-35s%-25s%-21s%-30s%-22s%-22s%-19s%-10s' % ('Normal Discount', self.handsetDiscount, 0, self.handsetDiscount, 0, (self.handsetDiscount)*-1, 0, 0, 0))
		if self.specialDiscount != 0:  # for case 10
			print('%-28s%-39s%-18s%-29s%-30s%-20s%-20s%-19s%-10s' % ('Special Discount', self.specialDiscount, 0, self.specialDiscount,0 ,0 ,0, 0, 0))
		if self.freeGoodsPrice != 0:
			print('%-28s%-35s%-25s%-21s%-30s%-22s%-22s%-19s%-10s' % ('Free goods thing', 0, round(self.revenueFreeGoods,2), 0, round(self.revenueFreeGoods,2) ,round(self.revenueFreeGoods, 2) ,0, 0, 0))
		print('-'*211)
		print('%-24s%-38s%-24s%-23s%-30s%-24s%-20s%-20s%s' % ('Total', round(self.sumTransAllPrice,2), round(self.sumRevenueComp,2), round(self.sumImmidateHandAndDisc,2), round(self.sumImmidateRev,2), round(self.sumImmidateContAsset,2), round(self.packagePrice,2), round(self.revenueCompPackPerMonth,2), round(self.diffRevenueCompPackPerMonth,2)))
		print('-'*211)
	
	def genEventBill(self):
		collect_actual = []
		collect_accured = []
		collect_revAccured = []

		date_list_actual = []
		trans_list_accured = [] # for use in reverse accured
		period = 1

		package_value = self.packagePrice
		actual_value = 0 # real usage value
		accured_value = 0 # estimate usage valuegi
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

			#billCycleInform loop
			period+=1
			trans_month+=1
			collect_actual.append(actual_value)
			collect_accured.append(accured_value)
			collect_revAccured.append(reverse_accured_value)
		print('')
		print('Actual Transaction:',collect_actual)
		print('Accured Transaction:',collect_accured)
		print('Reverse Accured Trasnaction:',collect_revAccured)


	#def showReport(self):
	#	pass
		#print('')
		#Output.scenarioInput(self)
		#b = Output()
		#print('')
		#Output.contractTransactionPrice(self)
		#print('')
		#b.allocating()
		#print('')
		#b.calculateContractAsset()
		#print('')
		#b.genEventBill()
		#print('')


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
	
	def addDecimal(self, a):
		if a.find('.') == -1:
			con_a = str(a)
			con_a+='.00'
			a = float(con_a)
		return a

class BillCycle(Output):

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

	def billCycleInform(self, date):
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
input('Press any key to exit..')


#	def calculatePeriod(self):
		#duration, start_contract, package_price, change_package_date, chnage_packate_price
#		base_formula = BaseFormula()
#		period = 0
		# When we want to inherite data from main class, we need to active main class first
		
		#duration = Output.duration_contract
		#start_contract = Output.start_contact
		#end_contract = Output.end_contract
		#package_price = Output.package_price
		#change_package_date = Output.change_package_date
		#change_package_price = Output.change_package_price

		#day1, month1, year1 = self.base_formula.cuttingString(start_contract)
		#day2, month2, year2 = self.base_formula.cuttingString(end_contract)
		#day3, month3, year3 = self.base_formula.cuttingString(change_package_date)

		#while duration+1 != period:
		#	if month1 == 13:
		#		month1=1
		#		year1+=1
		#	if month1 == month3 and year1 == year3:
		#		if package_price < change_package_price:
		#			return period
		#		elif package_price > change_package_price:
		#			return period
		#		else:
		#			return None
		#	period+=1
		#	month1+=1
			
			

#class CalculationDuration(Output):

#	def __init__(self):
#		print(Output.durationContract)
	
#	def calculatePeriod(self, startContract, endContract, changeServiceDate):
#		pass
		
		
		#period = 1
		#day1, month1, year1 = self.base_formula.cuttingString(startContract)
		#day2, month2, year2 = self.base_formula.cuttingString(endContract)
		#day3, month3, year3 = self.base_formula.cuttingString(changeServiceDate) # upgrade date

		#duration = self.base_formula.collectTotalMonth(month1, year1, month2, year2)
		#while duration != period-1:
		#	if month1 == 13:
		#		month1 = 1
		#		year1+=1
		#	print(day1, month1, year1)
		#	month1+=1
		#	period+=1
		



