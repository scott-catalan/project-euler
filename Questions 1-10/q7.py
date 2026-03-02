#What is the 10001st prime number?

import math as m

number = 3
prime_index = 1

def primes_up_to(n):
    full_list = [x for x in range(2, n)]

    num = 2
    while num * num <= n:
        full_list = [x for x in full_list if x == num or x % num != 0]
        for next_num in full_list:
            if next_num > num:
                num = next_num
                break
    
    return full_list

primes_up_to_10000 = primes_up_to(10000)

def check_if_prime(number):
    for i in primes_up_to_10000:
        if i > m.sqrt(number):
            break
        elif number % i == 0:
            return False
    return True

while True:
    if check_if_prime(number):
        prime_index += 1
    if prime_index >= 10001:
        break
    number += 2

print(number)