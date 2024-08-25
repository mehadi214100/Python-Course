number = int(input("Enter a number: "))

count = 0
while number != 0:
    count += 1
    number //= 10

print("Number of digits:", count)
