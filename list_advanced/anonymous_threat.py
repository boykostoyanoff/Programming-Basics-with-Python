words_list = input().split(' ')
while True:
    command_info = input()
    if command_info == '3:1':
        break
    command_info = command_info.split(' ')
    command = command_info[0]
    if command == 'merge':
        starting_index = int(command_info[1])
        end_index = int(command_info[2])
        if starting_index < 0:
            starting_index = 0
        if end_index >= len(words_list):
            end_index = len(words_list) - 1
        for i in range(starting_index + 1, end_index + 1):
            words_list[starting_index] += words_list[i]

        words_list = words_list[:starting_index + 1] + words_list[end_index + 1:]

    elif command == 'divide':
        index = int(command_info[1])
        partitions = int(command_info[2])

        element_for_divide = words_list[index]

        if partitions > len(element_for_divide):
            continue

        one_part_length = len(element_for_divide) // partitions
        elements_for_insert = list()

        for i in range(0, partitions):
            if i < partitions - 1:
                element_for_append = element_for_divide[i * one_part_length: (i + 1) * one_part_length]
            else:
                element_for_append = element_for_divide[i * one_part_length:]

            elements_for_insert.append(element_for_append)

        words_list = words_list[:index] + elements_for_insert + words_list[index + 1:]


print(' '.join(words_list))