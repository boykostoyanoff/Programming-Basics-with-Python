fragments = {'shards': 0,
             'fragments': 0,
             'motes': 0
             }
legendary_fragments = {'shards': 'Shadowmourne',
                       'fragments': 'Valanyr',
                       "motes": 'Dragonwrath'
                       }
item_name = None
while True:
    if item_name:
        break
    materials_info = input().split(' ')
    for i in range(0, len(materials_info), 2):
        if item_name:
            break
        fragment_name = materials_info[i + 1].lower()
        fragment_quantity = int(materials_info[i])

        if fragment_name not in fragments.keys():
            fragments[fragment_name] = 0
        fragments[fragment_name] += fragment_quantity

        if fragment_name in legendary_fragments.keys():
            if fragments[fragment_name] >= 250:
                fragments[fragment_name] -= 250
                item_name = legendary_fragments[fragment_name]

print(f'{item_name} obtained!')
for fragment, count in fragments.items():
    if fragment in legendary_fragments.keys():
        print(f'{fragment}: {count}')

fragments = dict(sorted(fragments.items(), key=lambda x: x[0], reverse=True))
for fragment, count in fragments.items():
    if fragment not in legendary_fragments.keys():
        print(f'{fragment}: {count}')
