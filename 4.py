x=int(input())
a='I'
b1='IV'
b='V'
c1='IX'
c='X'
d1='XL'
d='L'
e1='XC'
e='C'
s=''
if x==100:
    s+=e
else:
    if x//10==4:
        s+=d1
        if x%10==4:
            s+=(a+b) 
        elif x%10==9:
            s+=(a+c)
        else:
            if x%10<4:
                s+=(x%10)*a
            else:
                s+=b+((x%10)-5)*a
    else:
        if x//10==9:
            s+=e1
            if x%10==4:
                s+=(a+b)
            elif x%10==9:
                s+=(a+c)
            else:
                if x%10<4:
                    s+=(x%10)*a
                else:
                    s+=b+((x%10)-5)*a
        else:
            if x>=50:
                s+=d+((x-50)//10)*c
                if x%10==4:
                    s+=(a+b)
                elif x%10==9:
                    s+=(a+c)
                else:
                    if x%10<4:
                        s+=(x%10)*a
                    else:
                        s+=b+((x%10)-5)*a
            else:
                s+=(x//10)*c
                if x%10==4:
                    s+=(a+b)
                elif x%10==9:
                    s+=(a+c)
                else:
                    if x%10<4:
                        s+=(x%10)*a
                    else:
                        s+=b+((x%10)-5)*a
print(s)