def list_bodyguard(generic_list: list) -> list:
    unique_list = []
    for element in generic_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

my_list = list(input("Write elements to a list, separated by commas: ").strip().split(","))
print(list_bodyguard(my_list))