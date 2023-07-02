def is_prime(sayı):
    if sayı <= 1:
        return False
    for i in range(2, int(sayı ** 0.5) + 1):
        if sayı % i == 0:
            return False
    return True


step = 0
num = 2

while True:
    if is_prime(num):
        step += 1
        if step == 10001:
            print(num)
            break
    num += 1

# Output: 104743
