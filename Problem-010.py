import time

def sum_primes(number):
    sum, sieve = 0, [True] * number
    for p in range(2, number):

        if sieve[p]:
            sum += p
            for k in range(p * p, number, p):
                sieve[k] = False

    return sum


start = time.time()
print(sum_primes(2000000))
end = time.time()

print(end - start)