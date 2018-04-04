def shuffile_using_randint(x):
"""This function is use to suffle the iterable object using randint"""
    for f in range(len(x)):
        a = randint(0, len(x)-1)
        b = randint(0, len(x)-1)
        x[a], x[b] = x[b], x[a]
    print(x)
