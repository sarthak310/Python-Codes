n=int(input())
d=3
sum=0
while(d!=n+1):
	if(d%3==0 or d%5==0):
		sum=sum+d
		d=d+1
	else:
		d=d+1
print(sum)
