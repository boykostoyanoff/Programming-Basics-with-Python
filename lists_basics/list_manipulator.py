numbers = input().split(' ')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

command_info = input()

while not command_info == 'end':

    command_info = command_info.split(' ')
    if command_info[0] == 'exchange':
        index = int(command_info[1])
        if 0 <= index < len(numbers):
            numbers = numbers[index + 1:] + numbers[:index + 1]
        else:
            print('Invalid index')

    elif command_info[0] == 'max':
        result = 'No matches'
        is_number = False
        if command_info[1] == 'odd':
            n = 1
        elif command_info[1] == 'even':
            n = 0
        for i in range(len(numbers)):
            if numbers[i] % 2 == n:
                is_number = True
                result = i
                break
        if is_number:
            max_number = numbers[result]
            for i in range(len(numbers)):
                if numbers[i] % 2 == n:
                    if numbers[i] >= max_number:
                        max_number = numbers[i]
                        result = i
        print(result)

    elif command_info[0] == 'min':
        result = 'No matches'
        is_number = False
        if command_info[1] == 'odd':
            n = 1
        elif command_info[1] == 'even':
            n = 0
        for i in range(len(numbers)):
            if numbers[i] % 2 == n:
                is_number = True
                result = i
                break
        if is_number:
            max_number = numbers[result]
            for i in range(len(numbers)):
                if numbers[i] % 2 == n:
                    if numbers[i] <= max_number:
                        max_number = numbers[i]
                        result = i
        print(result)

    elif command_info[0] == 'first':
        count = int(command_info[1])
        if count > len(numbers):
            print(f'Invalid count')
        else:
            result = []
            n = 0
            if command_info[2] == 'odd':
                n = 1
            for i in range(0, len(numbers)):
                if numbers[i] % 2 == n:
                    result.append(numbers[i])
            print(result[:count])

    elif command_info[0] == 'last':
        count = int(command_info[1])
        if count > len(numbers):
            print(f'Invalid count')
        else:
            result = []
            n = 0
            if command_info[2] == 'odd':
                n = 1
            for i in range(0, len(numbers)):
                if numbers[i] % 2 == n:
                    result.append(numbers[i])
            print(result[-count:])

    command_info = input()

print(numbers)