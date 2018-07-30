n=int(input())
d=1
f1=1
f2=1
print(f1)
print(f2)
while(d!=n-1):
	sum=0
	sum=sum+f1+f2
	print(sum)
	f1=f2
	f2=sum
	d=d+1
	
