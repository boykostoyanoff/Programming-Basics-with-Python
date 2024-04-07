def possible_permutations(elements):
    if len(elements) <= 1:
        yield elements
        return
    for perm in possible_permutations(elements[1:]):
        for i in range(len(elements)):
            # nb elements[0:1] works in both string and list contexts
            yield perm[:i] + elements[0:1] + perm[i:]


[print(n) for n in possible_permutations([1, 2, 3])]