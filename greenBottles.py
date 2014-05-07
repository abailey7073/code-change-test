#Green bottles challenge
y = int(input("How many green bottles?"))
while y>0:
    print("{0} green bottles hanging on the wall.\n{0} Green bottles hanging on the wall.".format(y))
    print("And if one green bottle should accidentally fall,".format(y))
    y=y-1
    print("There'll be {0} green bottles hanging on the wall.".format(y))
