
end = input("Enter your number! ")
numbers = list()

while (end != ""): # Do it while end is not empty
    # --------- ? ---------- #
    if end == "":
        print("Here")
        continue
    # --------- ? ---------- #
    
    numbers.append(int(end))
    end = input("Enter your number! ")
else: # While also have else to
    operation = input("Enter the Operation!")
     
if operation == "+":
    print(numbers)
    sum_of_the_numbers = sum(numbers)
    print(f"Sum is {sum_of_the_numbers}")
elif operation == "-":
    sub_of_the_numbers = sum(numbers[1:])
    print(f"Subtraction is {numbers[0] - sub_of_the_numbers}")
elif operation == "*":
    mul = numbers[0]
    for i in range(1, len(numbers)): mul *= numbers[i]
    print(mul)
elif operation == "/":
    div = numbers[0]
    for i in range(1, len(numbers)): div /= numbers[i]
    print(div)