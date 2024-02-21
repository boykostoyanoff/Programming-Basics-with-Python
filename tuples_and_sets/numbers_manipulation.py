first_sequence = set(input().split(' '))
second_sequence = set(input().split(' '))

for idx in range(int(input())):
    command_info = input().split(' ')
    if command_info[0] == "Add":
        if command_info[1] == "First":
            first_sequence.update(command_info[2:])
        elif command_info[1] == "Second":
            second_sequence.update(command_info[2:])
    elif command_info[0] == "Remove":
        if command_info[1] == "First":
            first_sequence.difference_update(command_info[2:])
        elif command_info[1] == "Second":
            second_sequence.difference_update(command_info[2:])
    elif command_info[0] == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))


print(*sorted([int(x) for x in first_sequence]), sep=", ")
print(*sorted([int(x) for x in second_sequence]), sep=", ")
