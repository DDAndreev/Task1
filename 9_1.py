answ = 0

with open("9_1.csv", "r") as file:
    for line in file:
        row = sorted([int(i) for i in line.split(",")])
        if row[0]+row[1] > row[2] and row[0] == row[1] and row[2]**2 > 2*row[0]**2:
            print(row)
            answ += 1

print(answ)
