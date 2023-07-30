data = input()
data_list = data.split(', ')

count_of_beggars = int(input())
result = list()

for i in range(count_of_beggars):
    beggar_sum = 0
    for j in range(i, len(data_list), count_of_beggars):
        beggar_sum += int(data_list[j])

    result.append(beggar_sum)
print(result)