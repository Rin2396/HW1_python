a=int(input())
b=int(input())
if a==0:
    print('inf')
elif ((-b)//a)%1!=0:
    print('no')
else:
    print((-b)//a)