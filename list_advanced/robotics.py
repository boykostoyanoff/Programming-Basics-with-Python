from collections import deque


def add_time(current_time, time_to_add):
    h, m, s = current_time
    s += time_to_add
    if s > 59:
        m += s / 60
        s %= 60
        if m > 59:
            h += m / 60
            m %= 60
            if h > 11:
                h %= 12
    return [int(h), int(m), int(s)]


robots = list()
products = deque()

for robot in input().split(";"):
    if robot:
        name, time = robot.split("-")
        robots.append([name, int(time), 0])
time = [int(t) for t in input().split(":")]
is_end = False

while True:
    command = input()
    if command == "End":
        break
    products.append(command)

while products:
    time = add_time(time, 1)

    is_product_process = False
    product = products.popleft()
    for robot in robots:
        if robot[2] >= 1:
            robot[2] -= 1

        if robot[2] == 0 and not is_product_process:
            print(f"{robot[0]} - {product} [{time[0]:02}:{time[1]:02}:{time[2]:02}]")
            robot[2] = robot[1]
            is_product_process = True

    if not is_product_process:
        products.append(product)