from operator import truediv


def is_prime(n):
    factors = findFactors(n)
    if len(factors) == 2:
        return True
    else:
        return False
    

def findFactors(N):
    factors = []
    for i in range(1, N + 1):
        if N % i == 0:
            factors.append(i)

    return factors

def returnPrimes(lst):
    primes = []

    for num in lst:
        if is_prime(num):
            primes.append(num)
    
    return primes



def BAE(N):
    N = abs(N)
    if N == 0: return 0
    if N == 1: return 1

    factors = findFactors(N)
    primes = returnPrimes(factors)

    if is_prime(N):
        return 1 + BAE(N - 1)

    lst = []
    for prime in primes:
        temp = 1 + BAE(prime - 1) + BAE(N // prime)
        lst.append(temp)

    return min(lst)




print(findFactors(7))

print(BAE(100))