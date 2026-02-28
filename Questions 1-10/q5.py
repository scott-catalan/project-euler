#Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

#Time spent calculating on school chromebook: 11.37s

nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
current = 20

while True:
    indivisible_check = True
    for num in nums:
        if current % num != 0:
            indivisible_check = False
            break
    if indivisible_check:
        print(current)
        break
    current += 20
