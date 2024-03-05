def decart_product(list1, list2):
    decart_list = []
    for num in list1:
        index = []
        decart_list.append(index)
        for char in list2:
            index.append((num, char))
    return decart_list


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = ['a', 'b', 'c', 'd', 'e', 'f']
    decart_list = decart_product(list1, list2)
    for value in decart_list:
        print(value)
