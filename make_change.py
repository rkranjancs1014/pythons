#give change back for a note(make change algo)
coins = [1, 2, 3]
def number_Of_Ways(target):
    if (target < 0):
        return 0
    elif(target == 0):
        return 1
    else:
        return sum([numberOfWays(target - coin) for coin in coins])
