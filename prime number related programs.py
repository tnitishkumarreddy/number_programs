
# first n prime numbers
'''
n=int(input())
i=1
pc=0
while True:
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i)
            pc+=1
            if pc==n:
                break
    i+=1


# nth prime number

n=int(input())
i=1
pc=0
while True:
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            pc+=1
            if pc==n:
                print(i)
                break
    i+=1
'''

# 5th to 10th prime numbers

i=1
pc=0
while True:
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            pc+=1
            if pc>=5 and pc<=10:
                print(i)
            if pc==10:
                break
    i+=1
