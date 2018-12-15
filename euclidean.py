def euclidean():
    print('elo')
    global num
    num = random.randrange(3,n)
    print('wylosowano',num)
    if num % 2 == 0:
        print('parzysta, losowanie')
        euclidean()
    else:
        print('sprawdzam',num)
        print('dla fi:',fi)
        if num == fi:
            euclidean()
        a = num
        b = fi
        print('para liczb:', a,b)
        while a != b:
            if a > b:
                a = a - b
            elif a < b:
                b = b - a
        print(a,b)
        if a == b == 1:
            return
        else:
            euclidean()
        
    

    
euclidean()
print(num)
