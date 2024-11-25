n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)


''' input n=5

iteration 1: it will extract 1 and multiply it to fact=1 so now fact=1x1=1
iteration 2: it will extract 2 and multiply it to fact=1 so now fact=1x2=2
iteration 3: it will extract 3 and multiply it to fact=2 so now fact=3x2=6
iteration 4: it will extract 4 and multiply it to fact=6 so now fact=6x4=24
iteration 5: it will extract 5 and multiply it to fact=24 so now fact=24x5=120

at last print fact=120

'''
