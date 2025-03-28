while True:
    name = input("Adventure Choose a name : ")
    print(f"Welcome  {name} to a New Adventure")
    while True:
        ans = input(
            ("Where Do You Want to Go: \n You can go to the left or to the right \nTo go left type left or else type right ").lower())

        if ans == "left":
            option = input(
                f"{name} you have arrived at the lake \n You can swim across the lake or walk across the shore \n To swim type swim or type walk ").lower()
            if option == "swim":
                print("You swam in the river but it was cold so you fell ill and died")
                break
            elif option == "walk":
                option = input(
                    "You decided to walk across the shore and arrived at a castle. \n You can decide to go inside the castle or go back. \n To go inside the castle type in or type else back ").lower()
                if option == "in":
                    option = input(
                        "You decided to go inside the castle\nThere came across a stranger in the castle \n You can decide to talk with the stranger or ignore him \n to talk with the stanger type talk or else type ig. ").lower()
                    if option == "talk":
                        print(
                            "The stranger gave you a bag full of golds!!!!\nYou became extremly Rich \nYou won the game \nCONGRATS :) !!!!! ")
                        quit()
                    if option == "ig":
                        print(
                            "You missed an golden opertunity to become filthy rich \nYOU LOSE :(..... ")
                        break
                if option == "back":
                    print(
                        "You decided to go back from where you came while half way through some bandits attacked you and killed you\nYOU LOSE :(....  ")
                    break
                else:
                    print("Invalid Option You Lose.....")
                    quit()

        if ans == "right":
            opt = input(f"{name} you have arrived at the watch tower\n You can decide to go inside the watch tower or go back\n To go inside the watch tower type in or type back ").lower()
            if opt == "in":
                opt = input(f"{name} You decided to go inside the watch tower\n There you met a beautiful Madien \n You  fell love with her \n You decided to confess your feeling to her \n To confess you feeling type feel or to not confess type not ").lower()
                if opt == "feel":
                    print("You have expressed you feelings to the madien and she accepted your confession.\n You are very happy\nCongrats!!!!!\nYou have won the game :) ")
                    quit()
                elif opt == "not":
                    print("You decided not to confess your feeling which pushed you into sadness and depression \n Due to extreme depression You died. \n YOU FAILED\nGAME OVER :(....... ")
                    break
                else:
                    print("Invalid option")
                    break

            elif opt == "back":
                print("You decided to not go inside the watch tower \n You lost the golden opertunity to met with the love of your life\n You became sad and depressed and commited sucide\n YOu LOST THE GAME :( ")
                break


# Default option if the user does not type correct option

        else:
            print("Invalid option")
            break
# Asking player whether they want to paly again or not
    restart = input(
        "Do you want to play again? \nType Y for yes and N for no ").lower()
    if restart != "y":
        print("Thanks for Playing!!!!")
        quit()
