


food_dict = {}
food1 = input("Enter a food you like: ")
food_dict[1] = food1
food2 = input("Enter another food you like: ")
food_dict[2] = food2
food3 = input("Enter another food you like: ")
food_dict[3] = food3
food4 = input("Enter another food you like: ")
food_dict[4] = food4
print(food_dict)
dis_like = int(input("Which of these do you want to get rid of: "))
del dis_like
print(sorted(food_dict.values()))