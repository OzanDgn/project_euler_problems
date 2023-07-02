start_number = 999999
result = 0
while True:
    first_step = start_number % 1000
    second_step = start_number // 1000
    if str(second_step) == str(first_step)[::-1]:
        for i in range(999, 99, -1):
            if start_number % i == 0:

                remain = start_number // i
                if len(str(remain)) == 3:
                    result = start_number
                    break
    if result != 0:
        print(result)
        break
    start_number -= 1

# Output: 906609