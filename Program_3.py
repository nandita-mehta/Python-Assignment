number_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
remove_duplicate_list = sorted(set(number_list), key=number_list.index)
for i in remove_duplicate_list:
     print(i)
