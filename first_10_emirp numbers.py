def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    return False


def reverse(n):

    rev=0
    while n>0:
        r=n%10
        n//=10
        rev=rev*10+r
    return rev


def isEmirp(n):
    if isPrime(n) and isPrime(reverse(n)) and n!=reverse(n):
        return True
    else:
        return False

def first_n(num):
    c=0
    i=1
    while True:
        if isEmirp(i):
            print(i)
            c+=1
            if c==num:
                break
        i+=1
first_n(10)
