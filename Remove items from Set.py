my_set = set([12,19,14,12,8,9])
while my_set:
    my_set.discard(max(my_set))
    print(my_set)
