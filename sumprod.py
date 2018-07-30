n=int(input())
a=int(input("enter 1 for product & 2 for sum "))
if(a==1):
	fac=1
	while(n>1):
		fac=fac*n
		n=n-1
	print(fac)
if(a==2):
	d=1
	sum=0
	while(d!=n+1):
		sum=sum+d
		d=d+1
	print(sum)
