def KFC(x):
    if x == 3:
        return
    
    KFC(x+1)
    KFC(x+1)
    print(x)

KFC(0)