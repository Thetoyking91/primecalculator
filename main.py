import time

primeList = [2]


def checkPrime(i):
    for p in primeList:
        if i % p == 0:
            return False
    return True


def calculatePrimes(n):
    for i in range(3, n):
        if checkPrime(i):
            primeList.append(i)


def main():
    try:
        count = int(input("Upper bound: "))
        startTime = time.perf_counter()
        calculatePrimes(count)
        stopTime = time.perf_counter()
        print(f"Primes: {primeList} \n Time: {stopTime - startTime} seconds")
    except ValueError:
        print("Please enter a number. ")


if __name__ == "__main__":
    main()
