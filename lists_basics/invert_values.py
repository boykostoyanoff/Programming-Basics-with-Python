string_list = input()
numbers_list = string_list.split(' ')

for index in range(len(numbers_list)):
    numbers_list[index] = int(numbers_list[index]) * -1

print(numbers_list)
