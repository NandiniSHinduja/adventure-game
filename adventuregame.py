print("welcome to my game")
name = input("what is your name?")
age = input("what is your age?")
print("hello", name, "you are", age)
answer = input("would you like to play this game?yes/no")
if answer == "yes":
    choice = input("great! would you like to go left or right?")
    if choice == "left":
        print("you fell in the gutter, you lost!")
    else:
        choose = input("great! you entered a cave,you see a lion, would you like to attack or run?")
        if choose == "attack":
            weapon = input("do you need a gun or a sword for attacking?")
            if weapon == "gun":
                reward = input("great! you killed the lion!do you need food or money as your reward?")
                if reward == "food":
                    print("good choice, you survived in the forest with this food, you won this game")
                else:
                    print("bad choice! what would anyone do with money in the forest?haha, you lost!")
            else:
                print("what made you think you could defeat a lion with a sword? you lost!")

        else:
            mode = input("would you like to swim across the river or climb on the mountain?swim/climb")
            if mode == "swim":
                print("the sharks in the river ate you! you lost ")
            else:
                print("you fell from the mountain because there was an earthquake, you lost!")
else:
    print("too bad")
