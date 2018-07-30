n=int(input("Enter current year: "))
d=1
while(d!=21):
	n=n+1
	if(n%4==0):
		if(n%100==0 and n%400!=400):
			continue
		else:
			print(n)
			d=d+1
	else:
		continue
