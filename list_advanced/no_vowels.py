vowels = ['a', 'o', 'u', 'e', 'i']
word = input()

result = ''.join([c for c in word if c not in vowels])

print(result)