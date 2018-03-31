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
		max_value = self.greatestNum(x, y, z)
		temp_x, temp_y, temp_z = x, y, z
		while max_value != 1:
			if temp_x%max_value == 0 and temp_y%max_value == 0 and temp_z%max_value == 0:
				temp_y/=max_value
				temp_x/=max_value
				temp_z/=max_value
				print(max_value, "flag pass")
			else:
				pass
			max_value-=1
		return int(temp_x), int(temp_y), int(temp_z)

	def leastCommon():
		pass

	def factorial(self, x):
		result = 1
		while x != 1:
			result*=x
			x-=1
		return result

	def extractComponent(self, x, result):
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


	


a = Calculate()
#print(a.greatestNum(99, 29, 22))



#print(a.extractComponent(234, []))