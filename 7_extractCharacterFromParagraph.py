para = input("Your Parargaph: ")
char = input("Enter the character: ")
counter = 0

for word in para:
    if word == char:
        counter += 1
print(f"\t{char.upper()} happend {counter}-Times")