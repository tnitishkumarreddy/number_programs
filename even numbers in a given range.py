a=int(input())
b=int(input())

for i in range(a,b+1):
    if i%2==0:
        print(i)

''' input

13
19

iteration 1: it will extract 13 and check 13 is even or not false so dont print it
iteration 2: it will extract 14 and check 14 is even or not true so  print it
iteration 3: it will extract 15 and check 15 is even or not false so dont print it
iteration 4: it will extract 16 and check 16 is even or not true so print it
iteration 5: it will extract 17 and check 17 is even or not false so dont print it
iteration 6: it will extract 18 and check 18 is even or not true so print it
iteration 7: it will extract 19 and check 19 is even or not false so dont print it

'''
