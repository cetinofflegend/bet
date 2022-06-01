print("***Bet Game Only for fun. We do not suggest you play Bets in real life!***")
import random
havewon= "false"
i = 10
while i < 11:
    if havewon == "true":
        balance = newbalance
    else:
        balance = 100
    havewon = "true"
    print"Your balance is",balance,"$"
    if balance == 0:
        print("You have lost all your money how sad :(")
        break
    soru2 = raw_input("Select Multiplier Count (Default is 2x, Max 5x, type help for help): ")
    if soru2 == "":
        print"Alright, the multiplier is set to 2x"
        soru3 = "2"
    elif soru2 == "1":
        print"Damn dude, I think 1x Multipler is not valid. Instead of 1x, I have selected 2x for you. Innit better?"
        print"Alright, the multiplier is set to 2x"
        soru3 = "2"
    elif soru2 == "help" or soru2 == "Help":
        print("Bet Game, You start with 100$, Select the multiplier count and bet. You cannot bet more than your balance.If you won, You will get 2x,3x,4x or 5x of the amount u bet (depends on which multiplier you select, by default it is 2x)")
        print("Made by iFrocy (cetinofflegend)")
        print("Discord: iFrocy#0001")
        print("(in case you asked for help, the multiplier has selected 2x as default. When the round ends, you can change it from 2x up to 5x)")
        soru3="2"
    elif soru2 > "5":
        print("good try, Multiplier has been selected 2x as default. We said maximum is 5x. Why don't you listen to us?")
        soru3="2"
    else:
        print"Multipler has been set to ",soru2,"x"
        soru3 = soru2
    soru1 = input("How much do you want to bet?: ")
    if soru1 > balance:
        print("How are you gonna bet more than your balance?, Instead of closing game, I have selected the amount of money to bet to 2. Innit better?")
        soru1 = 2
    newbalance = balance - soru1
    if soru3 == "2":
        soru = input("Type number between 1 - 6 (1 and 6 included): ")
        rasgele = random.randint(1, 6)
        if soru == rasgele:
            print"You had won! You won double of your bet!"
            newbalance = newbalance + soru1 * 2
        else:
            print"Unfortunately you had lost."
            
    if soru3 == "3":
        soru = input("Type number between 1 - 10 (1 and 10 included): ")
        rasgele = random.randint(1, 10)
        if soru == rasgele:
            print"You had won! You won triple of your bet!"
            newbalance = newbalance + soru1 * 3
        else:
            print"Unfortunately you had lost."
    if soru3 == "4":
        soru = input("Type number between 1 - 14 (1 and 14 included): ")
        rasgele = random.randint(1, 14)
        if soru == rasgele:
            print"You had won! You won 4x of your bet!"
            newbalance = newbalance + soru1 * 4
        else:
            print"Unfortunately you had lost."
    if soru3 == "5":
        soru = input("Type number between 1 - 18 (1 and 18 included): ")
        rasgele = random.randint(1, 18)
        if soru == rasgele:
            print"You had won! You won 5x of your bet!"
            newbalance = newbalance + soru1 * 5
        else:
            print"Unfortunately you had lost."        
