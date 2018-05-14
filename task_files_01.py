n = int(input())
p = int(input())
with open('data.txt') as f:
    s = f.read()
    s = s.split()

div_n = [i for i in s if int(i) % n == 0]
div_n = ' '.join(div_n)

#square_p = [pow(int(i),p) for i in s]
square_p = ''
for i in s:
    i = pow(int(i),p)
    square_p = square_p + str(i) + ' '


with open('out-1.txt', 'w') as f:
    f.write(div_n)

with open('out-2.txt', 'w') as f:
    f.write(square_p)
