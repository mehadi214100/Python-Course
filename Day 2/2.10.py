binary = input("Enter a binary number: ")

decimal = 0
power = 0
i = len(binary) - 1
while i >= 0:
    decimal += int(binary[i]) * (2 ** power)
    power += 1
    i -= 1

print("Decimal:", decimal)
