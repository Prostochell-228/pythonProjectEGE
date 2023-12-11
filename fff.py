line = input()
res = ''
for i in range(0, len(line) - 2):
    result = ''
    for j in range(i, i + 3):
        result += line[j]
    if result == 'кря':
        res += f'{i}, '
print(res[0:len(res) - 1])
