def fibo():
    stop = 0
    total = 0
    x = 1
    y = 1
    while True:
        x, y = y, x + y

        if y > 4000000:

            break
        else:
            if y % 2 == 0:
                total += y
        stop += 1

    return total

fibo()

# Output: 4613732