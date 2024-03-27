index = 1
with open("9_2.csv", "r") as file:
    for line in file:
        row = [int(i) for i in line.split(",")]
        if all(row.count(i) == 3 for i in set(row)):
            print(index, row)
            break
        index += 1
