vip_guests = set()
regular_guests = set()
invited_guests = set()

for idx in range(int(input())):
    invited_guests.add(input())

while True:
    guest = input()
    if guest == "END":
        break
    if guest in invited_guests:
        invited_guests.remove(guest)


print(len(invited_guests))
invited_guests = sorted(invited_guests, key=lambda x: x)
[print(g) for g in invited_guests]