def sum_of_square(num):  # 1^2 + 2^2 + 3^2 + .... + 100^2
    total = 0
    for i in range(1, num + 1):
        total += i ** 2

    return total

def square_of_sum(num):   # (1+2+3+...+100)^2
    total = 0
    for i in range(1,num+1):
        total += i
    return total **2

print(square_of_sum(100) - sum_of_square(100))

# Output: 25164150