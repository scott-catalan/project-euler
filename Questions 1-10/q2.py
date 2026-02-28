#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Time spent calculating on school chromebook: practically instant

fibonacci1, fibonacci2 = 0, 1
total = 0
current_term = 0

while fibonacci2 < 4000000:
    current_term = fibonacci1 + fibonacci2
    if current_term % 2 == 0:
        total += current_term
    fibonacci1, fibonacci2 = fibonacci2, current_term
print(total)
