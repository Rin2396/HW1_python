a=float(input())
b=float(input())
c=float(input())
#a!=0
d=b**2-4*a*c
if d>0: #уравнение имеет 2 корня, если дискриминант положителен
    print((-b+d**(0.5))/(2*a),(-b-d**(0.5))/(2*a))
elif d==0: #уравнение имеет 1 корень, если дискриминант равен 0
    print((-b)/(2*a)) 
#елси дискриминант отрицателен, то корней нет, вот так вот
#все решенеия находим через математические формулы 7-8 класса(коментить не буду)