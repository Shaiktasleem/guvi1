def sumofAP(n,a,d):
	sum=0
	j=0
	while j<n:
		sum=sum+a
		a=a+d
		j=j+1
	return sum
n,a,d=map(int,raw_input().split())
print(sumofAP(n,a,d))
