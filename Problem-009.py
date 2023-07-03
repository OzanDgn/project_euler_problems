def triplet():
    for a in range(1,667):
        for b in range(a,667):
            c = 1000-a-b
            if c**2 == b**2 + a**2:
                return a*b*c

print(triplet())
