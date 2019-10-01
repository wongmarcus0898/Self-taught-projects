def dice():
    import random
    result = []
    print("How many sides are there on the dice?")
    s = int(input())
    print("How many dices do you want?")
    d = int(input())
    for num in range(d):
        result.insert(num, (random.randint(1,s)))
    print("Rolls: " + str(result))