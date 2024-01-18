import random

def RollDice(dice_value, rolls):
    print("May the dice be ever in your favour")
    for i in range(0, rolls):
        d = random.randint(1, dice_value)
        print("___" +str(d)+ "---")
    print()
    
dice_value = [100, 20, 12, 8, 6, 4]
exit_option = len(dice_value) + 1
choice = 0

while choice != exit_option:
    for i in range(len(dice_value)):
        print(str(i + 1) + ". d" + str(dice_types[i]))
        
        print(str(exit_option) + ". exit")
        print()
        
        choice = int(input("Select die value, 100, 20, 12, 8, 6, 4: "))
        
        if(choice == exit_option):
            print("Luck always runs out.")
        else:
            rolls = int(input("Number of required dice: "))
            RollDice(dice_value[choice-1],rolls)