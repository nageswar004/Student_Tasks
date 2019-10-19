index = input("Enter a numbar :")
a = range(-10,1)

b = range(1,11)
a.extend(b)

if index in a:
	c=[]
	c=a.index(index)
	print(c)
else:
	print("Given value is not there")
