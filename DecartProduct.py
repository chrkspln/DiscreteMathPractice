def decart_product(list1, list2):
    decart_list = []
    for i in list1:
        line = []
        for j in list2:
            line.append((i, j))
        decart_list.append(line)
    return decart_list


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = ['a', 'b', 'c', 'd', 'e', 'f']
    decart_list = decart_product(list1, list2)
    for value in decart_list:
        print(value)
