a=int(input("Enter smaller num: "))
b=int(input("Enter bigger num: "))
d=a
while(d!=0):
	if(a%d==0 and b%d==0):
		print(d)
		break
	d=d-1
	
