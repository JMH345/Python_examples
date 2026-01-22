#Jimmy Halaz
#Final_Project
import roulette
the_wheel = roulette.RouletteWheel()

def allow_bet(mybank):
    '''determines if bet is a whole number positive integer less than bankroll'''
    answer3 = False
    while answer3 == False:
        try:
            b_amount = int(input("Please enter a dollar amount to bet (enter numerals only). "))
            if b_amount > 0:
                if mybank >= b_amount:
                    answer3 = True
                else:
                    print("You cannot bet more than your current bankroll. Current bankroll is ${:,d}.".format(mybank))
            else:
                print("Negative numbers are not allowed.")
        except ValueError:
            print("Only whole numbers are accepted.")
    return b_amount

def color_bet(mybank, b_amount, color_pick):
    '''determines amount of money won or lost by comparing picked color to winning slot after spinning wheel'''
    mybank -= b_amount
    the_wheel.spin()
    myslot = str(the_wheel.get_slot())
    print("The winning slot is", myslot)
    if color_pick in myslot.lower():
        mybank += (b_amount * 2)
        print("You win. Your bankroll is now ${:,d}.".format(mybank))
    else:
        print("You lost. Your bankroll is now ${:,d}.".format(mybank))
    return mybank

def single_number_bet(mybank, b_amount, num_pick):
    '''determines amount of money won or lost by comparing picked number to winning slot after spinning the wheel'''
    mybank -= b_amount
    the_wheel.spin()
    myslot = str(the_wheel.get_slot())
    comp_slot = ""
    for a in myslot:
        if a.isdigit() == True:
            comp_slot += a
    comp_slot = int(comp_slot)
    print("The winning slot is", myslot)
    if int(num_pick) == int(comp_slot):
        mybank += (b_amount * 35)
        print("You win. Your bankroll is now ${:,d}.".format(mybank))
    else:
        print("You lost. Your bankroll is now ${:,d}.".format(mybank))
    return mybank

def still_playing(mybank):
    '''determines if you have money to play and asks if you want to continue'''
    if mybank == 0:
        playing = "no"
        print("Your bankroll is empty.")
    else:
        again = False
        while again == False:
            playing = input("Would you like to continue betting? (yes or no) ")
            if playing.lower() != "yes" and playing.lower() != "no":
                print("Answer must be 'yes' or 'no'.")
            else:
                again = True
    return playing

def main():
    #set original bankroll amount
    bank_set = False
    while bank_set == False:
        try:
            mybank = int(input("Please enter an intial bankroll dollar amount (enter numerals only). "))
            if mybank > 0:
                origin_bank = mybank
                bank_set = True
            else:
                print("Only positive values are accepted.")
        except ValueError:
            print("Only whole dollar interger amounts are accepted.")
            
    #start betting sequence
    answer1 = False
    while answer1 == False:
        playing = input("Would you like to place a bet? (yes or no) ")
        if playing.lower() != "yes" and playing.lower() != "no":
            print("Answer must be 'yes' or 'no'.")
        else:
            answer1 = True
    
    #type of bet selection
    while playing == "yes":
        answer2 = False 
        while answer2 == False:
            bet_type = input("If you would like to place a color bet, enter 'color'. If you would like to enter a single number bet, enter 'single'. ")
            
            #color bet initialized and values assembled
            if bet_type.lower() == "color":
                answer2 = True
                #entering bet amount
                b_amount = allow_bet(mybank)
                #pick and validate color
                color_pick = "green"
                while color_pick != "black" and color_pick != "red":
                    color_pick = input("Would you like black or red (type 'black' or 'red')? ")
                    if color_pick != "black" and color_pick != "red":
                        print("Error. Only 'red' or 'black' may be entered")
                mybank = color_bet(mybank, b_amount, color_pick)
                playing = still_playing(mybank)
                    
            # single number bet initialized and values assembled
            elif bet_type.lower() == "single":
                answer2 = True
                #entering bet amount
                b_amount = allow_bet(mybank)
                #pick and validate number
                num_pick = 50
                while num_pick < 0 or num_pick > 36:
                    try:
                        num_pick = int(input("Pick a number between 0 and 36). ").strip())
                        if num_pick < 0 or num_pick > 36:
                            print("Error. Number out of range.")
                    except ValueError:
                        print("Value must be a integer.")
                mybank = single_number_bet(mybank, b_amount, num_pick)
                playing = still_playing(mybank)
                    
            else:
                answer2 = False
                print("Your answer must be 'color' or 'single'.")
    #endgame values            
    else:
        print("Your game is over.")
        print("You bankroll is ${:,d}.".format(mybank))
        winnings = mybank - origin_bank
        if winnings < 0:
            winnings = abs(winnings)
            print("You lost ${:,d}.".format(winnings))
        elif winnings > 0:
            print("You won ${:,d}.".format(winnings))
        else:
            print("You broke even.")
#activate         
start_program = main()