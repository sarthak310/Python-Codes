k=1
sum=0
while(k<=10**6):
	sum=sum+((-1)**(k+1))/((2*k)-1)
	k=k+1
print(4*sum)
