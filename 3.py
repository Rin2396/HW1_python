n=int(input())
if n>8:
    if n>34:
        if n>60:
            n3=n//60
            if n%60>34:
                n3+=1
            else:
                if (n%60)%10>8:
                    n1=0
                    n2=(n%60)//10+1
                else:
                    n1=n%10
                    n2=(n%60)//10
        else:
            n3=1
            n1=0
            n2=0
    else:
        n3=0
        if n%10>8:
            n1=0
            n2=n//10+1
        else:
            n1=n%10
            n2=n//10
else:
    n1=n
    n2=0
    n3=0
print(n1,n2,n3)