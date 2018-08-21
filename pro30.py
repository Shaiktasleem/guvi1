hr1,min1=map(int,raw_input().split())
hr2,min2=map(int,raw_input().split())
x1=hr1*60+min1
x2=hr2*60+min2
d=abs(x1-x2)
t=d%60
t1=(d-t)//60
print t1,t
