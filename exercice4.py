fruits_list = {1, 5, 7}
colors_list = {3, 8, 7}
print(fruits_list)
print(colors_list)

total_list = fruits_list.union(colors_list)
print(total_list)

total_list2 = fruits_list.intersection(colors_list)
print(total_list2)

difference_list = fruits_list.difference(colors_list)
print(difference_list)

fruits_list.add(9)
print(fruits_list)

fruits_list.remove(1)
print(fruits_list)
