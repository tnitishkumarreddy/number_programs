def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
s,c=0,0

for i in range(0,999):
    if isPrime(i):
        s+=i
        c+=1
print(s,c)
from math import *
print(ceil(s/c))
print(floor(s/c))
        
