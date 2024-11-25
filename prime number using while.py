n=int(input())
if n>1:
    a=2
    while a<n//2+1:
        if n%a==0:
            print(f'{n} is not a prinme number')
            break
        a+=1
    else:

        print(f'{n} is a prime number')
        
else:
    print(f'{n} is not a prime number')
