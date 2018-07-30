a=int(input())
b=int(input())
while(a<=b):
	num=a
	d=2
	while((num%d!=0) and (d!=num)):
		d=d+1
	if(d==num):
		print(num)
		print("prime")
	a=a+1
