a=int(input())
b=int(input())
while a<=b:
    print(a**2)
    a+=1


''' a=2 b=6

iteration 1: a=2 check a<=b(2<=6) true so print 2**2=4
iteration 2: a=3 check a<=b(3<=6) true so print 3**2=9
iteration 3: a=4 check a<=b(4<=6) true so print 4**2=16
iteration 4: a=5 check a<=b(5<=6) true so print 5**2=25
iteration 5: a=6 check a<=b(6<=6) true so print 6**2=36
iteration 6: a=7 check a<=b(7<=6) false so exit from the loop
