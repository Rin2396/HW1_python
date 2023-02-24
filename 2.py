x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
#I - x>0 y>0
#II - x<0 y>0
#III -  x<0 y<0
#IV - x>0 y<0
if x1*x2>0 and y1*y2>0: #координаты точек, находящихся в одной четверти, имеют один знак по OX и один знак по OY, а значит произведения координат по OX и координат по OY всегда положительны 
    print('YES')
else:
    print('NO')