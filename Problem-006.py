def sum_of_square(num):  # 1^2 + 2^2 + 3^2 + .... + 100^2
    toplam = 0
    for i in range(1, num + 1):
        toplam += i ** 2

    return toplam

def square_of_sum(num):   # (1+2+3+...+100)^2
    toplam = 0
    for i in range(1,num+1):
        toplam += i
    return toplam **2

print(square_of_sum(100) - sum_of_square(100))

# Output: 25164150