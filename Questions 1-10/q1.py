#Find the sum of all multiples of 3 and 5 below 1000

#Time spent calculating on school chromebook: practically instant

import math

first_multiple = 3
second_multiple = 5
multiple_cap = 1000

total = 0

lcm = (first_multiple * second_multiple) // math.gcd(first_multiple, second_multiple)

for i in range(first_multiple, multiple_cap, first_multiple):
    total += i

for i in range(second_multiple, multiple_cap, second_multiple):
    total += i
    
for i in range(lcm, multiple_cap, lcm):
    total -= i
    
print(total)
