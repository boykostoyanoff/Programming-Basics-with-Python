opens_parentheses = ("[", "(", "{")
close_parentheses = ("]", ")", "}")

parentheses = [x for x in input()]
idx = 0
while True:
    if idx == len(parentheses):
        break
    if parentheses[idx] in opens_parentheses:
        idx += 1
        continue
    i = close_parentheses.index(parentheses[idx])
    if parentheses[idx - 1] == opens_parentheses[i]:
        parentheses.pop(idx)
        parentheses.pop(idx - 1)
        idx -= 1
    else:
        break

if parentheses:
    print("NO")
else:
    print("YES")