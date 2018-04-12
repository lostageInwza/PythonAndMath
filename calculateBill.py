class BaseCalculation(object):

	def __init__(self, regisDate, handsetPrice, handsetDiscount, packagePrice, duration):
		self.regisDate = regisDate
		self.handsetPrice = handsetPrice
		self.handsetDiscount = handsetDiscount*-1
		self.packagePrice = packagePrice
		self.duration = duration
		self.list_value = [
			self.regisDate,
			self.handsetPrice,
			self.handsetDiscount,
			self.packagePrice, 
			self.duration
		]

	def cuttingString(self, a):
  		return int(a[0:2]), int(a[3:5]), int(a[6:10]) # a, b, c

	def billCycle(self):
		day, month, year = self.cuttingString(self.list_value[0])

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
			elif day in range(28, self.checkMonth(month, year)+1): # 28, end_month
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

	def upperPercentage(self, a):
  		list_a = list(a)
  		if int(list_a[6]) > 5:
  			if int(list_a[5]) == 9:
  				list_a[4] = str(int(list_a[4])+1)
  				list_a[5] = '0'
  				list_a[6] = ''
  			else:
  				list_a[5] = int(list_a[5])+1
  				list_a[6] = ''
  		else:
  			list_a[6] = ''
  		a = ''.join(list_a)
  		return a
  		

	def checkMonth(self ,month, year):
		if month in (1, 3, 5, 7, 8, 10, 12):
			return 31
		elif month in (4, 6, 9, 11):
			return 30
		else:
	   		if month == 2 and self.checkYear(year) == 366:
	   			return 29
	   		return 28

	def scenarioInput(self):
		a = self.list_value
		d = self.billCycle()
		print('**** SCENARIO INPUTS ****')
		print('Transaction Price: %s %s %s'% (a[1], a[2], a[3]))
		print('Standalone selling Price: %s 0 %s'% (a[1], a[3]))
		print("Rgsiter Date: ", a[0])
		print('Usage Date from:', d[0])
		print('Usage Date to:', d[1])
		print("Bill Cycle:", d[2])

	def priceHandset(self):
		a = self.list_value
		total_contract = (a[1]+a[2])+a[3]*12
		total_ssp = a[1]+a[3]*12
		print('**** CONTRACT TRANSACTION PRICE and STANDALONE SELLING PRICE ****')
		print("Transaction Price: %s %s %s \033[4m%s\033[0m" % (a[1], a[2], a[3]*12, round(total_contract, 4)))
		print('Total Contract SSP: %s %s \033[4m%s\033[0m' % (a[1], a[3], round(total_ssp, 4)))

	def allocating(self):
		a = self.list_value
		total_contract = (a[1]+a[2])+a[3]*12
		total_ssp = a[1]+a[3]*12
		percent_per_com_hand = (a[1] / total_ssp) * 100
		percent_per_com_pack = (a[3]*12 / total_ssp) * 100
		total_component = round(percent_per_com_hand, 2) + round(percent_per_com_pack, 2)
		revenue_allocated_hand = (percent_per_com_hand*total_contract)/100
		revenue_allocated_pack = (percent_per_com_pack*total_contract)/100
		print('**** ALLOCATING REVENUE TO COMPONENTS ****')
		print("Transaction Price: %s %s %s \033[4m%s\033[0m" % (a[1], a[2], a[3]*12, round(total_contract, 2)))
		print('Total Contract SSP: %s %s \033[4m%s\033[0m' % (a[1], a[3], round(total_ssp, 2)))
		print('Percent-per Components: %s%% %s%% \033[4m%s%%\033[0m'% (round(percent_per_com_hand, 2), round(percent_per_com_pack, 2), total_component))
		print('Revenue Allocating to Component: %s \033[4m%s\033[0m' % (round(revenue_allocated_hand, 2), round(revenue_allocated_pack, 2)))

	def calculating_asset(self):
		a = self.list_value
		total_contract = (a[1]+a[2])+a[3]*12
		total_ssp = a[1]+a[3]*12
		percent_per_com_hand = (a[1] / total_ssp) * 100
		percent_per_com_pack = (a[3]*12 / total_ssp) * 100
		total_component = round(percent_per_com_hand, 2) + round(percent_per_com_pack, 2)
		revenue_allocated_hand = (percent_per_com_hand*total_contract)/100
		revenue_allocated_pack = (percent_per_com_pack*total_contract)/100
		print('**** CALCULATING THE CONTRACT ASSET - Immediate and Ongoing Events ****')
		print("Total Cashflow: %s %s %s \033[4m%s\033[0m" % (a[1], a[2], a[3]*12, round(total_contract, 2)))
		print('Revenue Allocated to Component: %s %s \033[4m%s\033[0m' % (a[1], a[3], round(total_ssp, 2)))
		print('Immediate Cashflow: %s%% %s%% \033[4m%s%%\033[0m'% (round(percent_per_com_hand, 2), round(percent_per_com_pack, 2), total_component))
		print('Revenue Allocating to Component: %s \033[4m%s\033[0m' % (round(revenue_allocated_hand, 2), round(revenue_allocated_pack, 2)))


#print("\033[4m\033[0m") underline string

c = BaseCalculation(
	regisDate = '10/10/2018',
	handsetPrice = 32242.99,
	handsetDiscount = 4672.90,
	packagePrice = 599,
	duration = 12
			)

print('')
c.scenarioInput()
print("")
c.priceHandset()
print('')
c.allocating()
print('')



#class Output(object):
#	def __init__(self):
#		self.b = BaseCalculation(
#			regisDate = '10/10/2018',#regisDate = input('Register date: '),
#			handsetPrice = 32242.99,#handsetPrice = int(input('Handset price: ')),
#			handsetDiscount = 4672.90,#handsetDiscount = int(input('Handset discount: ')),
#			packagePrice = 599,#packagePrice = int(input('Package price: ')),
#			duration = 12#duration = int(input('Duration length: '))
#		)

#	def printer(self):
#		print(self.b.billCycle())


#a = Output()
#a.printer()
#print(b.billCycle())