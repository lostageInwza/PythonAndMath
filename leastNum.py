def extractComponent(x):
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
	
	
def checkPrimeNumber(x):
	check = extractComponent(x)
	if len(check) <= 2:
		return x # if return them self, it's prime number
	return -1 # if return -1, it's not prime number
	
def leastNum(x, y, z):
	numSet = []
	collect = 1
	temp_num = 1
	for a in x, y, z:
		numSet.append(a)
	length = len(numSet)
	
	while length != 0:
		pos=length+1
		length-=1
		if checkPrimeNumber(numSet[length]) == numSet[length]: # ถ้าเช็คแล้วคือจำนวนเฉพาะ นำไปคูณกับ Result และนำออกจาก array
			collect*=numSet[length]
			numSet.pop()
		else: # ถ้าไม่ใช่เป็นจำนวนเฉพาะจะเข้าลูปด้านล่าง
			while True:
				if numSet[length]%checkPrimeNumber(temp_num) == 0 and checkPrimeNumber(temp_num) == temp_num: # ถ้าจำนวนตำแหน่งดังกล่าวหาร กับ ตัวหารลงตัว  # ถ้าเลขหารดังกล่าวเป็นจำนวนเฉพาะ (ครน ต้องหารด้วยจำนวนเฉพาะ)
					result=numSet[length]/temp_num
					if pos > length:
						temp_num=0
						pos-=1
					else:
						collect*=result
						print(collect, length, numSet[length], temp_num)
				else:
					break
				temp_num+=1
	return collect
	
print(leastNum(19, 20, 18))
	
