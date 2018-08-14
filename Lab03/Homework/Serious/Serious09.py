def get_even_list(l):
    list_new =[]
    for i in l:
        if i%2 == 0:
            list_new.append(i)
    return list_new

result = print(get_even_list([1, 2, 5, -10, 9, 6]))