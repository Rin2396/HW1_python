k=int(input())
m=int(input())
n=int(input())
if k>=n:
    print(m*2)
elif n%k==0:
    print((n//k)*2*m)
else:
    print(((n//k)+1)*2*m)