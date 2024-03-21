budget = int(input())

while budget >= 0:
    gift = input()

    if gift == 'End':
        print('You bought everything needed.')
        break

    budget -= int(gift)
else:
    print(f'You went in overdraft!')
