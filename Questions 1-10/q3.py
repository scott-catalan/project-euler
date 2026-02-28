#Find the largest prime factor of 600851475143

#Time spent calculating on school chromebook: 1.13s

import math as m

num = 600851475143
factor_maximum = m.sqrt(num)
all_factors = []
possible_factor = 1
answer = 0
prime_found = False

def primes_up_to(n):
    prime = [True] * (n + 1)
    prime[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return [i for i, is_prime in enumerate(prime) if is_prime]

while possible_factor < factor_maximum:
    if num % possible_factor == 0:
        all_factors.append(possible_factor)
    possible_factor += 1

divisibility_check = primes_up_to(all_factors[-1])

for factor in reversed(all_factors):
    if factor in divisibility_check:
        answer = factor
        break

print(answer)
