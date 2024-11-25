a=int(input())
b=int(input())
s=0
for i in range(a,b+1):
    s+=i
print(s)

''' input a=1 b=5

iteration 1: it will extract 1 and add it to s=0 so now s=0+1=1
iteration 2: it will extract 2 and add it to s=1 so now s=1+2=3
iteration 3: it will extract 3 and add it to s=3 so now s=3+3=6
iteration 4: it will extract 4 and add it to s=6 so now s=6+4=10
iteration 5: it will extract 5 and add it to s=10 so now s=10+5=15

at last print s=15
'''

