#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product of abc.

a = 0
b = 0
c = 0

N = 333

for a in range(1, N):
    for b in range(a, N):
        for c in range(b, N):
            if a**2 + b**2 == c**2:
                print(a, b, c)