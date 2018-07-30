n=100
m=999
while(n<=m):
	sum=0
	temp=n
	while(temp!=0):
		d=temp%10
		sum=sum+d**3
		temp=temp//10
		if(sum==n):
			print(n)
			print("armstrong num")
	n=n+1
