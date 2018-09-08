n=int(raw_input())
x=1
y=1
count=0
if(n==0):
	print(n)
elif(n<0):
	print("enter the valid number")
else:
	while(count<n):
		print x,
		term=x+y
		x=y
		y=term
		count+=1
