number = int(input("Enter a number: "))

sum_digits = 0
while number != 0:
    sum_digits += number % 10
    number //= 10

print("Sum of digits:", sum_digits)
