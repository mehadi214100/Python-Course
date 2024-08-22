import math

a = float(input('Enter 1st side: '))
b = float(input('Enter 2nd side: '))
c = float(input('Enter 3rd side: '))

if (a + b) > c and (b + c) > a and (c + a) > b:
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)
else:
    print('Triangle is not valid')
