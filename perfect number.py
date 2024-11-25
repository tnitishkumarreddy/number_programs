n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print(f'{n} is perfect number')
else:
    print(f'{n} is not a perfect number')

''' input n=6

iteration 1: it will extract 1 and check whether 6 is perfectly divisible by 1 true so add it sum so s=0+1=1
iteration 2: it will extract 2 and check whether 6 is perfectly divisible by 2 true so add it sum so s=1+2=3
iteration 3: it will extract 3 and check whether 6 is perfectly divisible by 3 true so add it sum so s=3+3=6
iteration 4: it will extract 4 and check whether 6 is perfectly divisible by 4 false so still s=6
iteration 5: it will extract 5 and check whether 6 is perfectly divisible by 5 false so still s=6

now check whether sum s=6 is equal to n=6 true so print n is a perfect number

'''
