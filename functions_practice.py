def hello():
    print("Hello fellow human")

def pack( x, y, z):
    return [x, y, z]

def eat_lunch(lunch):
    if len(lunch) == 0:
        print ("My lunchbox is empty")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I eat {lunch[0]}")
            else:
                print(f"Next I eat {lunch[i]}")

hello()
print(pack("x", "y", "z"))
print(pack("I", "am", "human"))
eat_lunch([])
eat_lunch(["Chipotle"])
eat_lunch(["salad", "Chipotle", "cookie", "water"])