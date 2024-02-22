from collections import deque

materials = [int(m) for m in input().split(' ')]
magics = deque([int(m) for m in input().split(' ')])
presents = {"Doll": 150,
            "Wooden train": 250,
            "Teddy bear": 300,
            "Bicycle": 400
            }
presents_crafted = {"Doll": 0,
                    "Wooden train": 0,
                    "Teddy bear": 0,
                    "Bicycle": 0
                    }

while magics and materials:
    magic = magics[0]
    material = materials[-1]
    if material == 0 or magic == 0:
        if material == 0:
            materials.pop()
        if magic == 0:
            magics.popleft()
        continue
    total = magic * material
    if total < 0:
        material_to_add = magic + material
        materials.pop()
        magics.popleft()
        materials.append(material_to_add)
        continue
    if total not in presents.values():
        magics.popleft()
        materials[-1] += 15
        continue
    for name, price in presents.items():
        if total == price:
            presents_crafted[name] += 1
    magics.popleft()
    materials.pop()

if (presents_crafted["Doll"] > 0 and presents_crafted["Wooden train"]) or \
        (presents_crafted["Teddy bear"] > 0 and presents_crafted["Bicycle"]):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print("Materials left: ", end='')
    print(*materials[::-1], sep=', ')
if magics:
    print("Magic left: ", end="")
    print(*magics, sep=', ')
for name, count in sorted(presents_crafted.items()):
    if count > 0:
        print(f"{name}: {count}")
