def get_even_list(l):
    list_new =[]
    for i in l:
        if i%2 == 0:
            list_new.append(i)
    return list_new

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
