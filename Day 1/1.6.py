a = float(input('Enter 1st side: '))
b = float(input('Enter 2nd side: '))
c = float(input('Enter 3rd side: '))

if (a + b) > c and (b + c) > a and (c + a) > b:
    print('Triangle is valid')
else:
    print('Triangle is not valid')
