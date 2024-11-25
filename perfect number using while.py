a=int(input())
s=0
i=1
while i<a:
    if a%i==0:
        s+=i
    i+=1
if s==a:
    print(f'{a} is perfect number')
else:
    print(f'{a} is not perfect number')
