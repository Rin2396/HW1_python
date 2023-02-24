a=int(input())
b=''
if 10<a%100<20: # от 11 до 19 коров
    b='korov'
elif a%10==1: # 1 корова
    b='korova'
elif 1<(a%10)<5: # 2,3,4 коровы
    b='korovy'
else: # 5,6,7,8,9,10 коров
    b='korov'
print(a,b)