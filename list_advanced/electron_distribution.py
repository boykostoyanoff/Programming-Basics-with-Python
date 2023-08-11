number_of_electrons = int(input())

shells = []
n = 1

while 2 * n * n < number_of_electrons:
    current_shell = 2 * n * n
    shells.append(current_shell)
    n += 1
    number_of_electrons -= current_shell

if number_of_electrons > 0:
    shells.append(number_of_electrons)

print(shells)