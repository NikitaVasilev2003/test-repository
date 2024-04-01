force_words = ['сила', 'пребудет', 'с', 'тобой', 'Да']
print(force_words)
print('неизмененный список:', id(force_words))
last = force_words.pop()
first = force_words.pop(0)
force_words.insert(0, last)
force_words.append(first)
print(force_words)
print('измененный список:', id(force_words))

