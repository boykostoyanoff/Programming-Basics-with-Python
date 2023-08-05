initial_sequence = input().split(' ')
permutation_number = int(input())
index_to_remove = 0
result = '['
while initial_sequence:
    index_to_remove += permutation_number
    while index_to_remove > len(initial_sequence):
        index_to_remove -= len(initial_sequence)
    index_to_remove -= 1
    result += initial_sequence[index_to_remove] + ','
    initial_sequence.pop(index_to_remove)

result = result.rstrip(',') + ']'
print(result)