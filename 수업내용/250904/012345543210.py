def KFC(x):
    if x == 10:
        return
    
    print(x, end=' ')
    KFC(x+1)
    print(x, end=' ')

KFC(0)