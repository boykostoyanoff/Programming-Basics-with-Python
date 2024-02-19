parking = set()
for idx in range(int(input())):
    action, car_number = input().split(', ')
    if action == "IN":
        parking.add(car_number)
    elif action == "OUT":
        parking.discard(car_number)

if parking:
    for car in parking:
        print(car)
else:
    print(f"Parking Lot is Empty")