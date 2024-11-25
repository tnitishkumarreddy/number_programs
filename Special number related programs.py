
# given number is special number or not

n=int(input())
s=0
d=n
while d>0:
    r=d%10
    f=1
    for i in range(1,r+1):
        f*=i
    s+=f
    d//=10
if s==n:
    print('special number')
else:
    print('not a special number')


#Special numbers in a given range

ll=int(input())
ul=int(input())
for i in range(ll,ul+1):
    d=i
    s=0
    while d>0:
        r=d%10
        d//=10
        f=1
        for j in range(1,r+1):
            f*=j
        s+=f
    if s==i:
        print(s)


# first n special numbers

n=int(input())
c=0
i=1
while True:
    s=0
    d=i
    while d>0:
        r=d%10
        d//=10
        f=1
        for j in range(1,r+1):
            f*=j
        s+=f
    if s==i:
        print(i)
        c+=1
        if c==n:
            break
    i+=1



# nth special number

n=int(input())
c=0
i=1
while True:
    s=0
    d=i
    while d>0:
        r=d%10
        d//=10
        f=1
        for j in range(1,r+1):
            f*=j
        s+=f
    if s==i:
        c+=1
        if c==n:
            print(i)
            break
    i+=1

'''

# 2nd to 4th special number


c=0
i=1
while True:
    s=0
    d=i
    while d>0:
        r=d%10
        d//=10
        f=1
        for j in range(1,r+1):
            f*=j
        s+=f
    if s==i:
        c+=1
        if c>=2 and c<=4:
            print(i)
    if c==4:
        break
    i+=1



