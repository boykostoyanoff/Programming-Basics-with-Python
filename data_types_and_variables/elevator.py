peoples = int(input())
capacity = int(input())

courses = peoples // capacity

if peoples <= capacity:
    courses = 1
elif peoples % capacity > 0:
    courses += 1

print(courses)