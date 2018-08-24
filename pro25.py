def median(l,x):
       l.sort()
       if x%2==0:
       	return l[x/2]
       else:
       	return(l[x/2+1]+l[x/2])/2
x=int(raw_input())
i=[int(n) for n in raw_input().split()]
print(median(i,x-1))
