quantity_of_food = int(input())
orders = [int(o) for o in input().split(' ')]
complete_orders_message = "Orders complete"
not_complete_orders_message = "Orders left: "
current_order_number = 0

if orders:
    print(max(orders))
    while current_order_number < len(orders):
        quantity_of_food -= orders[current_order_number]
        if quantity_of_food < 0:
            print(not_complete_orders_message + " ".join(str(o) for o in orders[current_order_number:]))
            break
        current_order_number += 1

    if current_order_number == len(orders):
        print(complete_orders_message)