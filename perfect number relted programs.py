

# given number is perfect number or not
n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print(f'{n} is perfect number')
else:
    print(f'{n} is not a perfect number')



# first n perfect numbers

n=int(input())
i=1
c=0
while True:
    s=0
    for j in range(1,i//2+1):
        if i%j==0:
            s+=j
    if i==s:
        print(i)
        c+=1
        if c==n:
            break
    i+=1

# nth perfect number

n=int(input())
i=1
c=0
while True:
    s=0
    for j in range(1,i//2+1):
        if i%j==0:
            s+=j
    if i==s:
        c+=1
        if c==n:
            print(i)
            break
    i+=1


# 2nd to 4th perfect numbers



i=1
c=0
while True:
    s=0
    for j in range(1,i//2+1):
        if i%j==0:
            s+=j
    if i==s:
        c+=1
        if c>=2 and c<=4:
            print(i)
        if c==4:
            break
    i+=1
