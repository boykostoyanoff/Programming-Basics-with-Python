def fill_the_box(height, length, width, *args):
    volume = height * length * width
    volume -= sum(args[:args.index("Finish")])

    if volume >= 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {abs(volume)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))