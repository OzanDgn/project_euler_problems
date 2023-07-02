def gcd(a, b):  # gcd = greatest common divisor
    if a == b:
        return a

    else:
        while True:
            if a == 0 or b == 0:
                break
            elif a > b:
                a %= b
            else:
                b %= a

        return max(a, b)


sm_pos_number = 1
for i in range(2, 21):
    if sm_pos_number % i != 0:
        res = i // gcd(i, sm_pos_number)
        sm_pos_number *= res

print(sm_pos_number)

# Output: 232792560