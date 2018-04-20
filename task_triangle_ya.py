x1 = int (input())
y1 = int (input())
x2 = int (input())
y2 = int (input())
x3 = int (input())
y3 = int (input())

a = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
b = ((x1 - x3) ** 2) + ((y1 - y3) ** 2)
c = ((x2 - x3) ** 2) + ((y2 - y3) **2 )

if b <= a >= c and a == b + c:
    print ('yes')
elif a <= b >= c and b == a + c:
    print ('yes')
elif a <= c >= b and c == a + b:
     print ('yes')
else:
    print ('no')
