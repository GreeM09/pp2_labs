def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_list = [1, 7, 2, 3, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
print(unique_elements(input_list))
