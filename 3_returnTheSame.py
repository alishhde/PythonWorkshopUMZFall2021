

lst1 = [12, 34, 1, 4, 2, 3, 11, 57, 87, 5, 4, 39, 27, 247, 2456]
lst2 = [34, 12, 45, 78, 94, 365, 87, 53, 4, 39, 233, 247, 2456]

same_list = list()
for element in lst1:
    if element in lst2:
        same_list.append(element)
        
print(same_list)


# In class


# lst1 = [1, 2, 3, 23, 23,5, 2,3 , 23,3535,46,5,675,5,75,7]
# lst2 = [21, 2, 3, 233, 234,55, 25,3 , 623,83535,46,5,675,54,75,73]
# lst = list()
# for element in [21, 2, 3, 233, 234,55, 25,3 , 623,83535,46,5,675,54,75,73]:
#     if element in lst1:
#         lst.append(element)
# print(lst)