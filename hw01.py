for i in range(1,10):
    for n in range (1,i):
        print(end='       ')
    for j in range (i,10):
        print('%dx%d=%2d' %(i,j,i*j), end=' ')
    print()