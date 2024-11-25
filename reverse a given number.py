n=int(input())
re=0
while n>0:
    r=n%10
    re=re*10+r
    n//=10
print(re)

'''

n=int(input())
l=[]
while n>0:
    r=n%10
    l.append(r)
    n//=10
for i in l:
    print(i,end='')
'''
