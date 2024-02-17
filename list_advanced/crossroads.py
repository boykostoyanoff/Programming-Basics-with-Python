from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
cars_passed = 0
traffic = deque()
is_crash = False

while True:
    info = input()
    if info == "END":
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break
    if info == "green":
        green = green_light_duration
        while traffic and green > 0:
            car = traffic.popleft()
            car_time_to_pass = len(car)
            green -= car_time_to_pass
            if green <= 0:
                if free_window_duration < abs(green):
                    print("A crash happened!")
                    print(f"{car} was hit at {car[car_time_to_pass + green - free_window_duration]}.")
                    is_crash = True

            cars_passed += 1

        if is_crash:
            break
    else:
        traffic.append(info)