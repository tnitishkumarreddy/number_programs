n=int(input())
dum=n
s=0
while dum>0:
    r=dum%10
    s+=r
    dum//=10
if n%s==0:
    print(f'{n} is harshad number')
else:
    print(f'{n} is not a harshad number')
