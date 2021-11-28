

lst1 = [12, 34, 1, 4, 2, 3, 11, 57, 87, 5, 4, 39, 27, 247, 2456]
lst2 = [34, 12, 45, 78, 94, 365, 87, 53, 4, 39, 233, 247, 2456]

same_list = list()
for element in lst1:
    if element in lst2:
        same_list.append(element)
        
print(same_list)