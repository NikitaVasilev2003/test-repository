days = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
steps = [1500, 3445, 13222, 10000, 12555, 1300, 6000]
result = []
for i in range(len(days)):
    days_steps = days[i], steps[i]
    result.append(days_steps)
print(result)
