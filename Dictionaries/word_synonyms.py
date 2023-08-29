count = int(input())
synonyms = dict()

for i in range(count):
    key = input()
    value = input()
    if key not in synonyms.keys():
        synonyms[key] = list()
    if value not in synonyms[key]:
        synonyms[key].append(value)

for term in synonyms.keys():
    print(f'{term} - {", ".join(synonyms[term])}')