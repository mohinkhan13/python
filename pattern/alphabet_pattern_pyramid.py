count = 1
for i in range(65, 75):
    print(" " * (10 - count),(chr(i) + " ") * count)  # Print leading spaces
    count += 1