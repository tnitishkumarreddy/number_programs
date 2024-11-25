n=int(input())
m,sm=0,0
d=n
while d>0:
    r=d%10
    d//=10
    if r>m:
        m=r
while n>0:
    rem=n%10
    n//=10
    if rem<m and rem>sm:
        sm=rem
print(sm)
