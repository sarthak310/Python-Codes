t=input()
p=input()
count=0
for i in range(0,len(t)-len(p)+1):
	for j in range(0,len(p)):
		if t[i]==p[j]:
			i+=1
			if j==len(p)-1:
				count+=1
		else:
			break
print(count)
