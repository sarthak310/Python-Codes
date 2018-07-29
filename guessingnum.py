n=69
print("The coder has chosen a secret 2-digit number for you! FIND IT OUT!!")
print(" ")
t=1
m=int(input())
while(m!=n):
	if(abs(m-n)>50):
		print("Too large !!")
	elif(abs(m-n)<=50 and abs(m-n)>30):
		print("Large !")
	elif(abs(m-n)<=30 and abs(m-n)>10):
		print("Small :)")
	else:
		print("Too small :):)")
	t=t+1
	m=int(input())
print("Congratulations,you have got the number...")
print("No. of trials you took:",t)
