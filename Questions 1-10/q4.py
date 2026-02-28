#Find the largest palindrome made from the product of two 3-digit numbers.

#Time spent calculating on school chromebook: 0.54s

product_max = 999*999
answer = 0

for i in reversed(range(1, product_max + 1)):
    if str(i) == str(i)[::-1]:
        for a in range(100, 999):
            if i % a == 0:
                b = i // a
                if 100 <= b <= 999:
                    answer = i
                    break
    if answer != 0:
        break

print(answer)