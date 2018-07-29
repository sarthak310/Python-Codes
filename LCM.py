a=int(input("Enter smaller num: "))
b=int(input("Enter bigger num: "))
if(b%a==0):
	print(b)
else:
	m=b+1
	while(m<=a*b):
		m=m+1
		if(m%a==0 and m%b==0):
			print(m)
			break
