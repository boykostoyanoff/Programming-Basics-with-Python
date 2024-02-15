n = int(input())
deq = list()

for i in range(n):
    command = input().split()
    if command[0] == '1':
        deq.append(int(command[1]))
    elif deq:
        if command[0] == '2':
            deq.pop()
        elif command[0] == '3':
            print(max(deq))
        elif command[0] == '4':
            print(min(deq))
        else:
            continue
    else:
        continue
while deq:
    print(deq.pop(), end="")
    if deq:
        print(end=", ")
