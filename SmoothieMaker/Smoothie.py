# parts that have C-137 are incomplete but rest of the program works like a melon sorry in advanced


fridge = ([
    "strawberry", "banana",
    "pineapple", "mango",
    "peach", "honey",
    "ice", "yogurt",
    "raspberry","blueberry",
    "black currant", "grape juice",
    "frozen yogurt", "blackberry",
    "green apple", "kiwi",
    "lime", "avocado",
    "spinach", "apple juice",
    "soy milk", "passion fruit" ,
    "ice cream", "chocolate",
    "peanut", "cherry"
],)


Classic = ([
    "strawberry", "banana",
    "pineapple", "mango",
    "peach", "honey",
    "ice", "yogurt"
],)


Forest_Berry = ([
    "strawberry", "raspberry",
    "blueberry", "honey",
    "ice", "yogurt"
],)


Freezie = ([
    "blackberry", "blueberry",
    "black currant", "grape juice",
    "frozen yogurt"
],)


Greenie = ([
    "green apple", "kiwi",
    "lime", "avocado",
    "spinach", "ice",
    "apple juice"
],)


Vegan_Delite = ([
    "strawberry", "passion fruit",
    "pineapple", "mango",
    "peach", "ice",
    "soy milk"
],)


Just_Desserts = ([
    "banana", "ice cream",
    "chocolate", "peanut",
    "cherry"
],)


freezer = ({
    "0":[Classic , "Classic"] ,
    "1":[Forest_Berry , "Forest_Berry"] ,
    "2":[Freezie,"Freezie"] ,
    "3":[Greenie,"Greenie"] ,
    "4":[Vegan_Delite,"Vegan_Delite"] ,
    "5":[Just_Desserts,"Just_Desserts"]
},)


def IWannaMakeASmoothie():
    ItemsIWantFromFridge = input("How many ITEMS would you like to pick from fridge? ")
    try:
        ItemsIWantFromFridge = int(ItemsIWantFromFridge)
        print("Choose your ingredients: ")
        for i, a in enumerate(fridge[0]):
            print(f"{i}: {a}")
        LetMeMakeMyGoddamnSmothie(ItemsIWantFromFridge)
    except ValueError:
        print("Please enter a NUMBER: \n")
        IWannaMakeASmoothie()


def WantsSmoothieOrNot():
    WantsSmoothie = input("1.create your own Smoothie OR \n"
                          "2.choose a Smoothie from freezer: ")
    if WantsSmoothie.isnumeric():
        if WantsSmoothie == "1":
            IWannaMakeASmoothie()
        elif WantsSmoothie == "2":
            WantsSmoothieFromFreezer()
        else:
            print("\nPlease Enter 1 or 2\n")
            WantsSmoothieOrNot()
    else:
        print("\nPlease Enter 1 or 2\n")
        WantsSmoothieOrNot()


def LetMeMakeMyGoddamnSmothie(ItemsIWantFromFridge):
    UserSmoothie = ([],)
    for i in range(0,ItemsIWantFromFridge):
        while(True):
            ingredients = input("Enter the first indredient number:")
            if ingredients.isnumeric():
                if int(ingredients) <= len(fridge[0]) -1:
                    UserSmoothie[0].append(fridge[0][int(ingredients)])
                    break
                else:
                    print(f"Please enter a number between {0} AND {len(fridge[0]) -1}")
            else:
                print(f"Please enter a number between {0} AND {len(fridge[0]) -1}")

    while(True):
        SmoothieName = input("Enter the name for your custom Smoothie: ")
        if not SmoothieName:
            print(" \n Please enter something for the name \n ")
        else:
            SureAboutTheName = input(f"Are you sure about the name {SmoothieName} ? Y/N: ")
            if SureAboutTheName == "Y":
                print("Congrats to you lad YOU just made your Smoothie :)\n"
                      f"Here is your {SmoothieName} with the ingredients of {' ,'.join(UserSmoothie[0])}")
                break
            elif SureAboutTheName == "N":
                print(" \n Enter the name your sure of then \n ")
            else:
                print(" \n please enter Y/N\n ")


def WantsSmoothieFromFreezer():
    # :))))))))))))))))))))))))))))
    ff = freezer[0]["1"][1]
    lengthFreezer = len(freezer[0])
    for i in range(0,lengthFreezer):
        fridgeItems = freezer[0][str(i)][1]
        keys = list(freezer[0].keys())
        print(f"{keys[i]}: {fridgeItems}")

    while(True):
        print(" \n NOTE: Enter the correct name (CASE SENSITIVE) \n ")
        UserFreezerChoice = input("Which one do you want? (Classic): ")
        if UserFreezerChoice.isnumeric() or not UserFreezerChoice:
            pass
        else:
            for i in range(0,lengthFreezer):
                if not UserFreezerChoice == freezer[0][str(i)][1]:
                    pass
                else:
                    print(f"{UserFreezerChoice} ingredients are: {freezer[0][str(i)][0][0]}")
                    SendItToFunction = freezer[0][str(i)[0][0]]
                    WantsToChangeTheIngredients(UserFreezerChoice , SendItToFunction)
                    return False # Do NOT touch this or it will break



def WantsToChangeTheIngredients(UserFreezerChoice , SendItToFunction):
    while(True):
        WantsToTouchMyFreezer = input("do you want to change any of the items? Y/N ")
        if WantsToTouchMyFreezer == "Y" or WantsToTouchMyFreezer == "y":
            print(f"\nuse -{SendItToFunction[0][0][0]} to remove ingredients from {UserFreezerChoice} \n "
                  f"and +{SendItToFunction[0][0][2]} to add topping to {UserFreezerChoice} \n "
                  f"like this:+{SendItToFunction[0][0][3]},-{SendItToFunction[0][0][4]} :" )
            # C - 137 (does not check the user input for the correct ingredients)
            AddOrRemoveIngredients = input("")
            if AddOrRemoveIngredients.isnumeric():
                pass
            else:
                AddOrRemoveSignSplit = AddOrRemoveIngredients.split(",")
                AddOrRemoveSignSplitList = ([],)
                AddOrRemoveSignSplitList[0].append(AddOrRemoveSignSplit)
                for i in range(0,len(AddOrRemoveSignSplitList[0][0])):
                    PlusAndMinus = AddOrRemoveSignSplitList[0][0][i][0]
                    IngredientsNames = AddOrRemoveSignSplitList[0][0]
                    IPromiseThisIsTheLastFunction(IngredientsNames,PlusAndMinus , UserFreezerChoice)
            break
        elif WantsToTouchMyFreezer == "N" or WantsToTouchMyFreezer == "n":
            print(f"Here is your {UserFreezerChoice} Smoothie "
                  f"Mam with Ingredients of {SendItToFunction[0][0]} ")
            break
        else:
            print("Please enter Y/N OR y/n")


def IPromiseThisIsTheLastFunction(IngredientsNames,PlusAndMinus,UserFreezerChoice):
    for i in range(0, len(fridge[0])):
        for x in range(0,len(IngredientsNames)):
            IngredientsNamesSave = IngredientsNames[x][1:]
            fridgeSave = fridge[0][i]
            if IngredientsNamesSave == fridgeSave:
                Splitter= ''.join(IngredientsNames[x])
                TheLastFunction(Splitter,UserFreezerChoice)
            else:
                pass

def TheLastFunction(Splitter,UserFreezerChoice):
    for n in range(0,len(freezer[0])):
            if UserFreezerChoice == freezer[0][str(n)][1]:
                UserFreezerChoices = list(freezer[0][str(n)][0])
                TheEnd(Splitter, UserFreezerChoices)
            else:
                pass

def TheEnd(Splitter,UserFreezerChoices):

    while(True):
        # C-137 (prints the output of UserInput more than once but works fine :))) )
        # didn't have the time to fix the print for the last part hope rest of the program covers it with love HIRBOD AFLAKI
        if Splitter[0] == "+":
            if Splitter[1:] not in UserFreezerChoices[0]:
                UserFreezerChoices[0].append(Splitter[1:])
                print(UserFreezerChoices[0])
            else:
                pass
            break
        elif Splitter[0] == "-":
            if Splitter[1:] in UserFreezerChoices[0]:
                UserFreezerChoices[0].remove(Splitter[1:])
                print(UserFreezerChoices[0])
            else:
                pass
            break
        else:
            return False


WantsSmoothieOrNot()
