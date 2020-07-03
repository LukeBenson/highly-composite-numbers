from math import sqrt, ceil

def prime():
    primenums = [2,3]
    for i in range(4,1000000):
        for j in primenums:
            if i % j == 0:
                break
            elif j >= ceil(sqrt(i)):
                primenums.append(i)
                break
    return primenums

def hcn():

    N = int(input("Please enter the number of highly composite numbers u want: "))

    with open("highly-composite-numbers.txt","w") as file:
        file.write("These are the first " + str(N) + " Highly Composite Numbers\n")

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
                    factors.append(str(j))

            factorLen = len(factors) * 2

        else:
            for j in range(1,i+1):
                if i % j == 0:
                    factors.append(str(j))

            factorLen = len(factors)

        if factorLen > mostFactors:
            compNums.append(i)
            mostFactors = factorLen

            with open("highly-composite-numbers.txt","a") as file:
                file.write("HCN: " + str(i) + " - ")
                allfactors = factors
                if i > 36:
                    for factor in factors[::-1]:
                        allfactors.append(str(round(i/int(factor))))
                file.write("Factors: " + ",".join(allfactors) + " - ")
                file.write("Prime Composition: " + primeComp(i) + "\n")

        i += 1

def primeComp(i):

    primecomp = [str(1)]
    while i != 1:
        for y in primes:
            if i % y == 0:
                primecomp.append(str(y))
                i /= y
                break 
    return ",".join(primecomp)

primes = prime()
hcn()