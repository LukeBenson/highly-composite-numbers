from math import sqrt, ceil

N = int(input("Please enter the number of highly composite numbers u want: "))

compNums = []

mostFactors = 0

i = 1
while len(compNums) < N:

    factors = []

    if i % 6 != 0 and i > 6:
        i += 1
        continue

    if i > 36:
        for j in range(1,ceil(sqrt(i))):
            if i % j == 0:
                factors.append(j)

        factors = len(factors) * 2

    else:
        for j in range(1,i+1):
            if i % j == 0:
                factors.append(j)

        factors = len(factors)

    if factors > mostFactors:
        compNums.append(i)
        mostFactors = factors

        print(compNums, "we have", len(compNums), "so far")

    i += 1

with open("highly-composite-numbers.txt","w") as file:
    for i in compNums:
        file.write(str(i) + "\n")