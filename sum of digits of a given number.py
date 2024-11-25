n=int(input())
s=0
while n>0:
    r=n%10
    s+=r
    n//=10
print(s)


'''n=int(input())
s=str(n)
su=0
for i in s:
    su+=int(i)
print(su)'''
