def prim():
    primelist = []
    n_1 = 0
    n_2 = int(input())
    print("Prime numbers between", n_1, "and", n_2, "are:")

    for x in [*range(n_1, n_2), 1]:
        if x > 1:
            for i in [*range(2, x, 1)]:
                if (x % i) == 0:
                    break
            else:
                primelist.append(x)
    return primelist


prim()
