separator = ', '
single_string = input()
single_string_list = single_string.split(separator)
result = list()
zeroes = list()

for el in single_string_list:
    el = int(el)
    if el == 0:
        zeroes.append(el)
    else:
        result.append(el)

result.extend(zeroes)
print(result)
