counter1 = 0
counter2 = 0

with open("9_3.csv", "r") as file:
    for line in file:
        row = [int(i) for i in line.split(",")]
        if (row.count(2) == 0 and row.count(5) == 0):
            counter2 += 1
        elif (row.count(2) == 0 and row.count(3) == 0 and row.count(5) > row.count(4)):
            counter1 += 1
            
print(counter1/counter2)
