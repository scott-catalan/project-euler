#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Time spent calculating on school chromebook: practically instant

sum_of_squares = sum(i**2 for i in range(1, 101))
square_of_sum = sum((i for i in range(1, 101)))**2
answer = square_of_sum - sum_of_squares
print(answer)
