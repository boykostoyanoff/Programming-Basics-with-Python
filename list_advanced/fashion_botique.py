clothes_in_the_box = [int(c) for c in input().split()]
capacity_of_one_rack = int(input())
racks_used = 0
if clothes_in_the_box:
    racks_used += 1
current_rack = 0

for i in range(len(clothes_in_the_box)):
    current_rack += clothes_in_the_box[i]
    if current_rack > capacity_of_one_rack:
        racks_used += 1
        current_rack = clothes_in_the_box[i]
print(racks_used)