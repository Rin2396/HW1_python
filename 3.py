n=int(input())
if n>8: # билеты на 8 и менее поездок выгоднее купить, как 8 по 1 за 120р, чем 1 по 10 за 125р
    if n>34: # билеты на 34 и менее поездки выгоднее купить, как 3 по 10 и 4 по 1 за 435, чем 1 по 60 за 440р
        if n>60: 
            n3=n//60 # берем макс.число билетов по 60 поездок и остается некоторое число поездок меньше 60
            if n%60>34: # если оставшееся число поездок больше 34, то мы покупаем еще 1 билет по 60 поездок
                n3+=1
            else: # если меньше 34, то мы берем макс.число билетов по 10 поездок и остается некторое число поездок меньше 10
                if (n%60)%10>8: # если осталось больше 8 поездок, то покупаем еще 1 билет по 10 поездок
                    n1=0
                    n2=(n%60)//10+1
                else: # иначе покупаем столько билетов по 1 поездке, скольок поездок осталось
                    n1=n%10 
                    n2=(n%60)//10
        else:
            n3=1
            n1=0
            n2=0
    else: # если поездок меньше 34, то берем макс.число билетов по 10 поездок и остается некоторое число поездок меньшее 10
        n3=0
        if n%10>8: # если осталось больше 8 поездок, то покупаем еще 1 билет по 10 поездок
            n1=0
            n2=n//10+1
        else: # если осталось меньше 8 поездок, то покупаем столько же билетов по 1 поездке
            n1=n%10
            n2=n//10
else: # если поездок меньше 8, то покупаем столько же билетов по 1 поездке
    n1=n
    n2=0
    n3=0
print(n1,n2,n3)