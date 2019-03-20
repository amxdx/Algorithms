print("Equation: 8x + 6y = 2500")
for x in range(30,90):
	y = 250 - 8*x
	y = y/6
	if (y.is_integer()):
		print(x,y)

print("Equation: 9x + 6y = 2500")
for x in range(30,100,5):
	y = 2500 - 9*x
	y = y/6
	print(x,y)

