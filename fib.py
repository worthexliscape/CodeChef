def fib_ser(Number):
	if (Number==0):
		return 0
	elif(Number==1):
		return 1
	else:
		return (fib_ser(Number-2)+fib_ser(Number-1))

Number = int(input("\nRange: "))

for Num in range(0,Number):
		print(fib_ser(Num))