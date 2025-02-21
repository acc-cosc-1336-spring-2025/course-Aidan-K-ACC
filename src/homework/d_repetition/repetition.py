def get_factorial(num):
    fact = num
    for i in range(num):
        if i > 0:
            fact *= i
        i += 1
    return fact

def sum_odd_numbers(num):
    sum = 0
    i = 0
    while i <= num:
        if i%2 == 1:
            sum += i
        i += 1
    return sum
