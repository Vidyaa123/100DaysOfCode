print("WELCOME TO TREASURE ISLAND")
print("Your mission is to find the treaure")
print("Let's GO!!")
step1 = input("Do you want to go left or right - press l or r  :")
if step1 == "l" :
    print("You have reached a Lake")
    step2 = input("Do you want to swim or wait for a boat - press s or w :")
    if step2 == 'w':
        print("you take a boat and reach the island in the lake")
        step3 = input("There is a small cottage with three doors, red, blue and yellow - Press r,b or y to enter :")
        if step3 == 'r':
            print("You are burned... GAME OVER")
            exit()
        elif step3 == 'b':
            print("You are eaten by beasts...GAME OVER")
            exit()
        elif step3 == 'y':
            print("*****You have WON!! ---HURRAY*****")
            exit()
        else:
            print("Wrong Choice .. GAME OVER")
            exit()
    elif step2 == 's':
        print("You have been attacked by a Trout.. GAME OVER")
        exit()
    else:
        print("Wrong Choice.. GAME OVER")
elif step1 == 'r':
    print("You have fallen into a hole.. GAME OVER")
else:
    print("Wrong Choice.. GAME OVER")

