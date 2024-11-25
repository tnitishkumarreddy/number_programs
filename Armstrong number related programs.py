
# first n Armstrong numbers
'''
n=int(input())
i=1
c=0
while True:
    du=i
    l=len(str(i))
    s=0
    while du>0:
        r=du%10
        s+=r**l
        du//=10
    if i==s:
        print(i)
        c+=1
        if c==n:
            break
    i+=1


# nth Armstrong  number

n=int(input())
i=1
c=0
while True:
    du=i
    l=len(str(i))
    s=0
    while du>0:
        r=du%10
        s+=r**l
        du//=10
    if i==s:
        c+=1
        if c==n:
            print(i)
            break
    i+=1
'''

# 5th to 10th Armstrong numbers

i=1
c=0
while True:
    du=i
    l=len(str(i))
    s=0
    while du>0:
        r=du%10
        s+=r**l
        du//=10
    if i==s:
        c+=1
        if c>=5 and c<=10:
            print(i)
        if c==10:
            break
    i+=1

    
