# удалить повторяющиеся элименты вариант№1
def delete_recurring_number(list_1, list_2):
    for i in range(len(list_1) - 1, -1, -1):
        for elem2 in list_2:
            if list_1[i] == elem2:
                del list_1[i]
    return list_1


# удалить повторяющиеся элименты вариант№2
def delete_recurring_number_2(list, list_2):
    for number in list[:]:
        if number in list_2:
            list.remove(number)
    return list


if __name__ == '__main__':
    my_list_1 = [2, 5, 8, 2, 6, 124, 12, 12, 4]
    my_list_2 = [2, 7, 124, 12, 3, 6]
    print(delete_recurring_number(my_list_1, my_list_2))

    my_list_1 = [2, 5, 8, 2, 6, 12, 12, 4]
    my_list_2 = [2, 7, 12, 3]
    print(delete_recurring_number_2(my_list_1, my_list_2))
