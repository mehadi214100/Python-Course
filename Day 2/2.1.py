char = input("Enter a character: ")

if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
    print("Alphabet")
elif '0' <= char <= '9':
    print("Digit")
else:
    print("Special Character")
