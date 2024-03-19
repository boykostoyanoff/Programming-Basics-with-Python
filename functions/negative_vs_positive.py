def sum_positives(numbers: list):
    if not numbers:
        return 0
    return sum([n for n in numbers if n > 0])


def sum_negatives(numbers: list):
    if not numbers:
        return 0
    return sum([n for n in numbers if n < 0])


nums = [int(n) for n in input().split()]

print(sum_negatives(nums))
print(sum_positives(nums))

if sum_positives(nums) > (sum_negatives(nums) * -1):
    print(f"The positives are stronger than the negatives")
else:
    print(f"The negatives are stronger than the positives")