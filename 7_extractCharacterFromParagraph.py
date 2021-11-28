para = input("Your Parargaph: ")
char = input("Enter the character: ")
counter = 0

for i in para:
    if i == char:
        counter += 1
print(f"The {char} happend {counter}-Times")