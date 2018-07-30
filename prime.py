n=int(input())
d=2
flag=0
while(d!=n):
	if(n%d==0):
		print("non prime")
		flag=1
		break
	else:
		d=d+1
if(flag==0):
	print("prime")
