id_string = '32 48 2 6 14 58 2 88 9 14 123 48 3 17 42 42 7'
id_string1 = id_string.split(' ')
list_id_string = [int(id_1) for id_1 in id_string1]
new_set = set()
for list_id in list_id_string:
    if list_id in new_set:
        print(f'Найден дубликат {list_id}')
    new_set.add(list_id)
print(sorted(new_set))

