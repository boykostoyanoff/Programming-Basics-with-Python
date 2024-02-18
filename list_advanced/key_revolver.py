from collections import deque

price_of_each_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(b) for b in input().split(' ')]
locks = deque([int(l) for l in input().split(' ')])
value_of_intelligence = int(input())
idx = min(len(bullets), len(locks))
bullets_in_gun_barrel = size_of_gun_barrel

while bullets and locks:
    bullets_in_gun_barrel -= 1
    value_of_intelligence -= price_of_each_bullet
    if bullets[-1] <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    bullets.pop()
    if bullets_in_gun_barrel == 0 and bullets:
        bullets_in_gun_barrel = size_of_gun_barrel
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence}")