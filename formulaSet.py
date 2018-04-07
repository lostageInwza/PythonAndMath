class Calculate:

	def __init__(self):
		pass

	def maxNum(self, x, y):
		if x > y:
			return x
		return y
	
	def greatestNum(self, x, y, z):
		result = self.maxNum(self.maxNum(x, y), z)
		return result

	def greatestCommon(self, x, y, z):
		result = 0
		max_value = self.greatestNum(x, y, z)
		temp_x, temp_y, temp_z = x, y, z
		while max_value != 1:
			if temp_x%max_value == 0 and temp_y%max_value == 0 and temp_z%max_value == 0:
				temp_y/=max_value
				temp_x/=max_value
				temp_z/=max_value
				result = max_value
			else:
				pass
			max_value-=1
		return int(temp_x), int(temp_y), int(temp_z), result

	def duplicate_list(self, x):
		check = []
		for r in x:
			if r not in check:
				check.append(r)
			pass
		return check

	def factorial(self, x):
		result = 1
		while x != 1:
			result*=x
			x-=1
		return result

	def extractComponent(self, x):
		result = []
		temp_x = x
		x = 1
		while x != temp_x:
			if temp_x % x == 0:
				result.append(x)
			else:
				pass
			x+=1
		result.append(temp_x)
		return result
	
	def checkPrimeNumber(self,x):
		check = self.extractComponent(x)
		if len(check) <= 2:
			return x # if return them self, it's prime number
		return -1 # if return -1, it's not prime number

	def leastCommon(self, x, y, z):
		collect = []
		divider = 1
		for a in x, y, z:
			collect.append(a)
		arrange_list = sorted(collect)
		length = len(arrange_list)
		temp_length = length-1
		length-=1
		count = 0
		while arrange_list != [1, 1, 1]:
			if arrange_list[length]%divider == 0 and self.checkPrimeNumber(divider) == divider:
				print(arrange_list[length], divider)
				#if self.checkPrimeNumber(arrange_list[length]) == arrange_list[length]:
				#	divider=arrange_list[length]
				
			else:  
				pass
		return	arrange_list
a = Calculate()
print(a.leastCommon(42, 68, 32))
				
"""		
	def leastCommon(self, x, y, z): # <= 2
		resultList = []
		listNum = []
		divide_num = 1
		for a in x, y, z:
			listNum.append(a)
		pos = len(listNum)
		while pos != 0:
			pos-=1
			temp = listNum[pos]
			if self.checkPrimeNumber(listNum[pos]) == -1: # if a number is not a prime number, calculate least common
				while temp != 1:
					
					divide_num+=1
					if temp%divide_num == 0 and self.checkPrimeNumber(divide_num) != -1:
						count+=1
						temp = temp/divide_num # listNum[pos] = listNum[pos]/divide_num
						if temp != listNum[pos] and divide_num != 1:
							resultList.append(divide_num)
							
					if divide_num >= temp: # reset divide num, when it more than result
						divide_num = 0
			else: # if a number is a prime number, append to result list		
				resultList.append(listNum[pos])
		return resultList





		#extract and combine Result
		print(resultList)
		ans = []
		count = 0
		check = self.duplicate_list(sorted(resultList,  reverse=True)) # already sort numebr and cleaned number without duplicate, more to less
		check.pop(check.index(1)) # remove 1 from list		
		length_clean_list = len(check)

		#r = len(resultList)
		while length_clean_list != 0:
			length_clean_list-=1
			for a in resultList:
				pass
						
		return ans

"""				

