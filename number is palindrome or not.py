n=int(input())
dum=n
re=0
while dum>0:
    r=dum%10
    re=re*10+r
    dum//=10
if n==re:
    print(f'{n} is palindrome')
else:
    print(f'{n} is not a palindrome')
