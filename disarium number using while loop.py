n=int(input())
du=n
s=0
l=len(str(du))
while du>0:
    r=du%10
    s+=r**l
    l=l-1
    du//=10
if n==s:
    print(n,'is a disarium number')
else:
    print(n,'is not a disarium number')
