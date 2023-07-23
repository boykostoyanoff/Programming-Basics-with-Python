first_string = input()
second_string = input()

for i in range(len(first_string)):
    for j in range(len(first_string)):
        if not first_string[i] == second_string[i]:
            if j <= i:
                print(second_string[j], end='')
            else:
                print(first_string[j], end='')
        else:
            break
    else:
        print()
