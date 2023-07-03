import math

def is_prime(number):
<<<<<<< HEAD
    if number <= 1:
=======
    if sayı <= 1:
>>>>>>> 633860c43625079a0f8fccd0ac31653ad33e4168
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

number = 600851475143
largest_pri_fac = 0
for i in range(2,int(math.sqrt(number))+1):
    if number % i == 0:
        if is_prime(i):
            largest_pri_fac = i

print(largest_pri_fac)

# Output: 6857
