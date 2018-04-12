class BaseFormula(object):
	def cuttingString(self, a):
  		return int(a[0:2]), int(a[3:5]), int(a[6:10]) # a, b, c

class BillCycle(object):
	def billCycle(self):
		day, month, year = self.cuttingString()
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

class Output(object):
	def __init__(self):
		self.a = billCycle(
			startContract = '10/10/2018', #startContract = input('Register date: '),
			endContract = '11/10/2018',
		)
	def scenarioInput(self):
		print('**** SCENARIO INPUTS ****')
		print('Transaction Price: %s | %s | %s'% (self.a[1], self.a[2], self.a[3]))
		print('Standalone selling Price: %s | 0 | %s'% (self.a[1], self.a[3]))
		print("Rgsiter-Contract Date: \033[4m%s\033[0m"% self.a[0])
		print("End-Contract Date: \033[4m%s\033[0m"% self.a[1])
		print("Bill Cycle: \033[4m%s\033[0m" % self.b[2])
		print('Usage Date from: \033[4m%s\033[0m'% self.b[0])
		print('Usage Date to: \033[4m%s\033[0m' % self.b[1])


