string = input("Enter a string: ")

reverse = ""
i = len(string) - 1
while i >= 0:
    reverse += string[i]
    i -= 1

if string == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
