a=int(input())
b=''
if a%10==1:
    b='korova'
elif 1<(a%10)<5:
    b='korovy'
else:
    b='korov'
print(a,b)