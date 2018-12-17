def ex_euclidean():
    a = e
    b = fi
    u = 1
    x = 0
    w = a
    z = b
    while w != 0:
        if w < z:
            tym = w
            w = z
            z = tym
            tym = u
            u = x
            x = tym
        k = int(w / z)
        u = u - (k * x)
        w = w - (k * z)
    if x < 0:
        x = x + b
    d = x
    return d
ex_euclidean()
