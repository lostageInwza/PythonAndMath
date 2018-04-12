class BaseCalculation(object):

	def __init__(self, startContract, handsetPrice, endContract, handsetDiscount, packagePrice, duration):
		self.startContract = startContract
		self.endContract = endContract
		self.handsetPrice = handsetPrice
		self.handsetDiscount = handsetDiscount*-1
		self.packagePrice = packagePrice
		self.duration = duration
		self.list_value = [
			self.startContract,# 0
			self.endContract,# 1
			self.handsetPrice,# 2
			self.handsetDiscount,# 3
			self.packagePrice,# 4
			self.duration # 5
		]
		self.a = self.list_value
		self.b = self.billCycle()

		self.total_contract = (self.a[2]+self.a[3])+self.a[4]*self.duration
		self.total_ssp = self.a[2]+self.a[4]*self.duration

		self.percent_per_com_hand = (self.a[2] / self.total_ssp) * 100
		self.percent_per_com_pack = (a[3]*self.duration / self.total_ssp) * 100
		self.total_component = round(percent_per_com_hand, 2) + round(percent_per_com_pack, 2)
		self.revenue_allocated_hand = (percent_per_com_hand*total_contract)/100
		self.revenue_allocated_pack = (percent_per_com_pack*total_contract)/100
		self.total_revenue_allocated = revenue_allocated_hand + revenue_allocated_pack

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
		print('**** SCENARIO INPUTS ****')
		print('Transaction Price: %s | %s | %s'% (self.a[1], self.a[2], self.a[3]))
		print('Standalone selling Price: %s | 0 | %s'% (self.a[1], self.a[3]))
		print("Rgsiter-Contract Date: \033[4m%s\033[0m"% self.a[0])
		print("End-Contract Date: \033[4m%s\033[0m"% self.a[1])
		print("Bill Cycle: \033[4m%s\033[0m" % self.b[2])
		print('Usage Date from: \033[4m%s\033[0m'% self.b[0])
		print('Usage Date to: \033[4m%s\033[0m' % self.b[1])
		

	def priceHandset(self):
		print('**** CONTRACT TRANSACTION PRICE and STANDALONE SELLING PRICE ****')
		print("Transaction Price: %s | %s | %s | \033[4m%s\033[0m" % (self.a[2], self.a[3], self.a[4]*self.duration, round(self.total_contract, 4)))
		print('Total Contract SSP: %s | %s | \033[4m%s\033[0m' % (self.a[2], self.a[4]*self.duration, round(self.total_ssp, 4)))

	def allocating(self):
		print('**** ALLOCATING REVENUE TO COMPONENTS ****')
		print("Transaction Price: %s | %s | %s | \033[4m%s\033[0m" % (a[1], a[2], a[3]*12, round(total_contract, 2)))
		print('Total Contract SSP: %s | %s | \033[4m%s\033[0m' % (a[1], a[3], round(total_ssp, 2)))
		print('Percent-per Components: %s%% | %s%% | \033[4m%s%%\033[0m'% (round(percent_per_com_hand, 2), round(percent_per_com_pack, 2), total_component))
		print('Revenue Allocating to Component: %s | %s | \033[4m%s\033[0m' % (round(revenue_allocated_hand, 2), round(revenue_allocated_pack, 2), total_revenue_allocated))

	def calculating_asset(self):
		a = self.list_value
		total_contract = (a[1]+a[2])+a[3]*12
		total_ssp = a[1]+a[3]*12
		percent_per_com_hand = (a[1] / total_ssp) * 100
		percent_per_com_pack = (a[3]*12 / total_ssp) * 100
		total_component = round(percent_per_com_hand, 2) + round(percent_per_com_pack, 2)
		revenue_allocated_hand = (percent_per_com_hand*total_contract)/100
		revenue_allocated_pack = (percent_per_com_pack*total_contract)/100
		month_rev = round(int(revenue_allocated_pack)/int(self.duration),2) 
		print('**** CALCULATING THE CONTRACT ASSET - Immediate and Ongoing Events ****')
		print("Total Cashflow: %s | %s | %s | \033[4m%s\033[0m" % (a[1], a[2], a[3]*12, round(total_contract, 2)))
		print('Revenue Allocated to Component: %s | %s | \033[4m%s\033[0m' % (a[1], round(revenue_allocated_pack, 2), round(total_ssp, 2)))
		print('Immediate Cashflow: %s | %s | \033[4m%s\033[0m'% (a[1], a[2], a[1]+a[2]))
		print('Immediate Revenue: %s | \033[4m%s\033[0m' % (round(revenue_allocated_hand, 2), round(revenue_allocated_hand, 2)))
		print('Immediate Contract Asset: %s | %s | \033[4m%s\033[0m' % (round(revenue_allocated_hand, 2)-a[1], a[2]*-1, (round(revenue_allocated_hand, 2)-a[1]) + a[2]*-1))
		print('Monthly Cashflow: %s | \033[4m%s\033[0m' % (round(a[3],2), round(a[3],2)))
		print( 'Monthly Revenue: %s | \033[4m%s\033[0m'% (month_rev, month_rev))
		print('Monthly Contract Asset: %s | \033[4m%s\033[0m' % (month_rev-round(a[3],2), month_rev-round(a[3],2)))

	def monthlyCash(self):
		count = 0
		check = 0
		startBill, endBill, bc_name = self.billCycle()
		day, month, year = self.cuttingString(self.list_value[0])
		temp_month = self.list_value[4]
		while temp_month+1 != count:
			print('Event Date: %s/%s/%s' % (day, month, year))
			print('Event Date: %s/%s/%s' % (day, month, year))
			print('Event Date: %s/%s/%s' % (day, month, year))
			check+=1
			count+=1
			day = endBill
			if check == 1:
				check=0
				month+=1
				if count == temp_month:
					if self.checkYear(year) == 366:
						day = startBill
					else:
						day = startBill+1
				if month == 13:
					month=1
					year+=1
			
# if leap year return 'self'
# if not return self+1

#print("\033[4m\033[0m") underline string

c = BaseCalculation(
	startContract = '24/10/2018',
	endContract = '24/10/2019',
	handsetPrice = 32242.99,
	handsetDiscount = 4672.90,
	packagePrice = 599,
	duration = 6
		)

print('')
c.scenarioInput()
#print("")
#c.priceHandset()
#print('')
#c.allocating()
#print('')
#c.calculating_asset()
#print('')
#c.monthlyCash()


#class Output(object):
#	def __init__(self):
#		self.b = BaseCalculation(
#			startContract = '10/10/2018',#startContract = input('Register date: '),
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