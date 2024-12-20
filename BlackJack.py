#Murph Lennemann



import random
import math

#The function uses a for loop to create a deck and then uses a random number to get the index of a card
def DeckSetup():
    SuitList=["Hearts","Diamonds","Clubs","Spades"]
    SpecialNumList=["Ace","Jack","Queen","King"]
    DeckList=[]
    for suits in SuitList:
        for nums in range (2,11):
            DeckList.append(f'{str(nums)} of {suits}')
        for special in SpecialNumList:
            DeckList.append(f'{special} of {suits}')

    ShuffleList=[]
    while len(DeckList)!=0:
        length=len(DeckList)
        shufflenum=random.randint(0,length-1)
        ShuffleList.append(DeckList[shufflenum])
        DeckList.pop(shufflenum)
    return ShuffleList


#The function checks the part of the card before the first space to determine the value and adds them up
def DeckCounter(Deck):
    count=0
    SpecialNumList = ["Ace", "Jack", "Queen", "King"]
    for cards in Deck:
        space = cards.find(' ')
        number=cards[:space]
        if number in SpecialNumList:
            if number!="Ace":
                count+=10
            else:
                count+=11
        else:
            count+=int(number)

#Checks to see if there is an ace and then checks if it has gone over, if it has then it removes 10 for each ace as long as that ace has not been removed already.
    AceCount=0
    while count>21 and AceCount<(Deck.count("Ace of Hearts")+Deck.count("Ace of Diamonds")+Deck.count("Ace of Spades")+Deck.count("Ace of Clubs")):
        count-=10
        AceCount+=1
    return count

#Checks to see if the two cards delt have the same value.
def SplitCheck(Deck):
    List=[]
    for cards in Deck:
        space = cards.find(' ')
        number=cards[:space]
        List.append(number)
    if List.count(List[0])==2:
        Split=True
    else:
        Split=False
    return Split

#This is the logic behind the computer player. Uses percentages to make choices with a movie refernce thrown in.
def P2Player(Deck):
    HitChance=random.randint(1,100)
    if Deck==["2 of Spades","3 of Clubs"] or Deck==["3 of Clubs","2 of Spades"]:
        print("Dealer: 5")
        print("Computer: I'll Stay")
        print("Dealer: I suggest you hit sir")
        print("Computer: I also like to live dangerously")
        print("Dealer: As you wish sir")
        Move="Stay"
    elif DeckCounter(Deck)>21:
        Move="Bust"
    elif DeckCounter(Deck)<12:
        Move="Hit"
    elif DeckCounter(Deck)==12:
        if HitChance>=3:
            Move="Hit"
        else:
            Move="Stay"
    elif DeckCounter(Deck)==13:
        if HitChance>=8:
            Move="Hit"
        else:
            Move="Stay"
    elif DeckCounter(Deck)==14:
        if HitChance>19:
            Move="Hit"
        else:
            Move='Stay'
    elif DeckCounter(Deck)==15:
        if HitChance>38:
            Move="Hit"
        else:
            Move=("Stay")
    elif DeckCounter(Deck)==16:
        if HitChance>50:
            Move="Hit"
        else:
            Move="Stay"
    elif DeckCounter(Deck)==17:
        if HitChance>38:
            Move="Stay"
        else:
            Move="Hit"
    elif DeckCounter(Deck)==18:
        if HitChance>19:
            Move="Stay"
        else:
            Move="Hit"
    elif DeckCounter(Deck)==19:
        if HitChance>=8:
            Move="Stay"
        else:
            Move="Hit"
    elif DeckCounter(Deck)==20:
        if HitChance>2:
            Move="Stay"
        else:
            Move="Hit"
    else:
        Move="Stay"
    return Move

#Logic to determine if the computer should split based on what some website told me was good advice (IDK anything about strategy)
def P2Split(Deck,DealerDeck):
    SpecialNumList = ["Jack", "Queen", "King"]
    spacer = DealerDeck[1].find(' ')
    DealUp = DealerDeck[1][:spacer]
    space = Deck[0].find(' ')
    number=Deck[0][:space]
    Split='l'
    if number=='Ace' or number==8 or number==4:
        Split='True'
    elif number==10 or number in SpecialNumList or number==4 or number==5:
        Split=='True'
    elif number==9:
        if DealUp==7 or DealUp==10 or DealUp in SpecialNumList or DealUp=='Ace':
            Split='False'
        else:
            Split='True'
    elif number==7:
        if DealUp==2 or DealUp==3 or DealUp==4 or DealUp==5 or DealUp==6 or DealUp==7:
            Split='True'
        else:
            Split='False'
    elif number==6:
        if DealUp==2 or DealUp==3 or DealUp==4 or DealUp==5 or DealUp==6:
            Split = 'True'
        else:
            Split = 'False'
    elif number==3:
        if DealUp==4 or DealUp==5 or DealUp==6 or DealUp==7:
            Split='True'
        else:
            Split='False'
    elif number==2:
        if DealUp==4 or DealUp==5 or DealUp==6 or DealUp==7:
            Split='True'
        else:
            Split='False'
    return Split

#This gives the logic and the play of the dealer.
def DealerPlay(DealerHand,ResultsDict,DeckOfCards):
    print(f"The dealer's hand is:")
    print(DealerHand)
    print(f"The dealer's total is {DeckCounter(DealerHand)}")
    enter=input("Hit enter to continue")
    while DeckCounter(DealerHand)<=16:
        print("The dealer hits")
        print(f'The dealer has drawn the {DeckOfCards[0]}')
        DealerHand.append(DeckOfCards[0])
        DeckOfCards.pop(0)
        print(f"The dealer's hand is:")
        print(DealerHand)
        print(f'The dealer\'s total is {DeckCounter(DealerHand)}')
        enter=input("Hit enter to continue")
    if DeckCounter(DealerHand)>21:
        DealerHand.clear()
        print("The dealer busts")
    else:
        print("The dealer stays")
    ResultsDict["Dealer"]=DeckCounter(DealerHand)

#This plays through the turn of the second player, including the logic for a split.
def P2Turn(P2Hand,DealerHand,ResultsDict,DeckOfCards):
    print(f"The computer's hand is:")
    print(P2Hand)
    print(f"The computer's total is {DeckCounter(P2Hand)}")
    enter=input("Hit enter to continue")
    SplitHand=[]
    if SplitCheck(P2Hand)=="True":
        if P2Split(P2Hand,DealerHand):
            SplitHand.append(P2Hand[0])
            P2Hand.pop(0)
            P2Hand.append(DeckOfCards[0])
            SplitHand.append(DeckOfCards[1])
            DeckOfCards.pop(0)
            DeckOfCards.pop(0)
            print("The computer has decided to split")
            print(f"The computer's hands are {P2Hand} and {SplitHand}")
            enter=input("Press enter to continue")
            print(f"Starting with the {SplitHand} hand.")
            while P2Player(SplitHand) == "Hit" and DeckCounter(SplitHand) <= 21:
                print("The computer hits")
                print(f'The computer has drawn the {DeckOfCards[0]}')
                SplitHand.append(DeckOfCards[0])
                DeckOfCards.pop(0)
                print(f"The computer's hand is:")
                print(SplitHand)
                print(f'The computer\'s total is {DeckCounter(SplitHand)}')
                enter = input("Press Enter to continue")
            if DeckCounter(SplitHand) > 21:
                SplitHand.clear()
                print("The computer busts")
            else:
                print("The computer stays")
            ResultsDict['P2Split']=DeckCounter(SplitHand)
            print(f"Moving on to the {P2Hand} hand.")
    while P2Player(P2Hand)=="Hit" and DeckCounter(P2Hand)<=21:
        print("The computer hits")
        print(f'The computer has drawn the {DeckOfCards[0]}')
        P2Hand.append(DeckOfCards[0])
        DeckOfCards.pop(0)
        print(f"The computer's hand is:")
        print(P2Hand)
        print(f'The computer\'s total is {DeckCounter(P2Hand)}')
        enter = input("Press Enter to continue")
    if DeckCounter(P2Hand)>21:
        P2Hand.clear()
        print("The computer busts")
    else:
        print("The computer stays")
    ResultsDict["P2"]=DeckCounter(P2Hand)

#This is the logic for the players turn.
def PlayerTurn(PlayerHand,ResultsDict,DeckOfCards):
    print(f"{Name}'s hand is:")
    print(PlayerHand)
    print(f"The {Name}'s total is {DeckCounter(PlayerHand)}")
    SplitHand = []
    if SplitCheck(PlayerHand)=="True" and bet*2<=NameDict[Name]:
        splitchoice=input("Would you like to Split?\n").capitalize()
        while splitchoice!="Yes" and splitchoice!="No":
            print("Please respond with Yes or No,")
            splitchoice = input("Would you like to Split (This will double your bet)?\n").capitalize()
        if splitchoice=="Yes":
            SplitHand.append(PlayerHand[0])
            PlayerHand.pop(0)
            PlayerHand.append(DeckOfCards[0])
            SplitHand.append(DeckOfCards[1])
            DeckOfCards.pop(0)
            DeckOfCards.pop(0)
            print(f"The {Name}'s hands are {PlayerHand} and {SplitHand}")
            print(f"Starting with the {SplitHand} hand.")
            choice=input("Would you like to hit or stay?\n").capitalize()
            while choice!="Hit" and choice!="Stay":
                print("Please respond with hit or stay")
                choice=input("Would you like to hit or stay?\n").capitalize()
            while choice=="Hit" and DeckCounter(SplitHand)<=21:
                print(f"You drew the {DeckOfCards[0]}")
                SplitHand.append(DeckOfCards[0])
                DeckOfCards.pop(0)
                print(f"Your new hand is {SplitHand}")
                print(f"Your total is {DeckCounter(SplitHand)}")
                while choice != "Hit" and choice != "Stay":
                    print("Please respond with hit or stay")
                    choice = input("Would you like to hit or stay\n").capitalize()
            if DeckCounter(SplitHand)>21:
                SplitHand.clear()
                print(f'{Name} busted')
            ResultsDict['PlayerSplit']=DeckCounter(SplitHand)
            print(f"Moving on to the {PlayerHand} hand.")
    choice = input("Would you like to hit or stay?\n").capitalize()
    while choice != "Hit" and choice != "Stay":
        print("Please respond with hit or stay")
        choice = input("Would you like to hit or stay?\n").capitalize()
    while choice == "Hit" and DeckCounter(PlayerHand) <= 21:
        print(f"You drew the {DeckOfCards[0]}")
        PlayerHand.append(DeckOfCards[0])
        DeckOfCards.pop(0)
        print(f"Your new hand is {PlayerHand}")
        print(f"Your total is {DeckCounter(PlayerHand)}")
        if DeckCounter(PlayerHand)<=21:
            choice = input("Would you like to hit or stay\n").capitalize()
            while choice != "Hit" and choice != "Stay":
                print("Please respond with hit or stay")
                choice = input("Would you like to hit or stay\n").capitalize()
    if DeckCounter(PlayerHand) > 21:
        PlayerHand.clear()
        print(f'{Name} busted')
    ResultsDict[Name] = DeckCounter(PlayerHand)

#This gives the general logic for the order of the game, skipping over turns if there is a blackjack or both players bust
def PlayGame():
    DeckOfCards=DeckSetup()
    ResultsDict={"BlackJack":[]}
    if TwoMode=="Yes":
        PlayerHand=[DeckOfCards[0],DeckOfCards[3]]
        P2Hand=[DeckOfCards[1],DeckOfCards[4]]
        DealerHand=[DeckOfCards[2],DeckOfCards[5]]
        DeckOfCards.pop(0)
        DeckOfCards.pop(0)
        DeckOfCards.pop(0)
        DeckOfCards.pop(0)
        DeckOfCards.pop(0)
        DeckOfCards.pop(0)
    else:
        PlayerHand=[DeckOfCards[0],DeckOfCards[2]]
        DealerHand = [DeckOfCards[1], DeckOfCards[3]]
        DeckOfCards.pop(0)
        DeckOfCards.pop(0)
        DeckOfCards.pop(0)
        DeckOfCards.pop(0)
    try:
        if DeckCounter(PlayerHand) == 21:
            ResultsDict["BlackJack"].append(Name)
            ResultsDict[Name]=22
        if DeckCounter(P2Hand) == 21:
            ResultsDict["BlackJack"].append("The computer")
            ResultsDict['P2']=22
        if DeckCounter(DealerHand) == 21:
            ResultsDict["BlackJack"].append("The dealer")
            ResultsDict['Dealer']=22
    except:
        if DeckCounter(PlayerHand) == 21:
            ResultsDict["BlackJack"].append(Name)
            ResultsDict[Name]=22
        if DeckCounter(DealerHand) == 21:
            ResultsDict["BlackJack"].append("The dealer")
            ResultsDict['Dealer']=22
    print(f"The dealer is showing {DealerHand[1]}")
    if Name not in ResultsDict["BlackJack"] and "The dealer" not in ResultsDict["BlackJack"]:
        PlayerTurn(PlayerHand,ResultsDict,DeckOfCards)
    elif Name in ResultsDict["BlackJack"]:
        print(f"{Name} has blackjack")
    else:
        ResultsDict[Name]=0
    if "The computer" not in ResultsDict["BlackJack"] and TwoMode=="Yes" and "The dealer" not in ResultsDict["BlackJack"]:
        P2Turn(P2Hand,DealerHand,ResultsDict,DeckOfCards)
    elif "The computer" in ResultsDict['BlackJack'] and TwoMode=="Yes":
        print("The computer has BlackJack")
    elif TwoMode=="Yes":
        ResultsDict['P2']=0
    elif TwoMode=="Yes" and "The dealer" not in ResultsDict['BlackJack']:
        print("The computer has blackjack")
    try:
        if "The dealer" in ResultsDict['BlackJack']:
            ResultsDict['Dealer']=DeckCounter(DealerHand)
        elif Name in ResultsDict in ResultsDict['BlackJack'] and "The computer" in ResultsDict['BlackJack']:
            ResultsDict['Dealer']=DeckCounter(DealerHand)
        elif 'PlayerSplit' in ResultsDict and 'P2Split' in ResultsDict:
            if ResultsDict[Name]==0 and ResultsDict['P2']==0 and ResultsDict['PlayerSplit']==0 and ResultsDict['P2Split']==0:
                ResultsDict['Dealer']=DeckCounter(DealerHand)
        elif 'PlayerSplit' in ResultsDict:
            if ResultsDict[Name] == 0 and ResultsDict['P2'] == 0 and ResultsDict['PlayerSplit'] == 0:
                ResultsDict['Dealer']=DeckCounter(DealerHand)
        elif 'P2Split' in ResultsDict:
            if ResultsDict[Name] == 0 and ResultsDict['P2'] == 0 and ResultsDict['P2Split'] == 0:
                ResultsDict['Dealer']=DeckCounter(DealerHand)
        elif ResultsDict[Name]==0 and ResultsDict['P2']==0:
            ResultsDict['Dealer']=DeckCounter(DealerHand)
        else:
            DealerPlay(DealerHand,ResultsDict,DeckOfCards)
    except:
        if "The dealer" in ResultsDict['BlackJack']:
            ResultsDict['Dealer']=DeckCounter(DealerHand)
        elif Name in ResultsDict in ResultsDict['BlackJack']:
            ResultsDict['Dealer']=DeckCounter(DealerHand)
        elif 'PlayerSplit' in ResultsDict:
            if ResultsDict[Name] == 0 and ResultsDict['PlayerSplit']:
                ResultsDict['Dealer']=DeckCounter(DealerHand)
        elif ResultsDict[Name] == 0:
            ResultsDict['Dealer']=DeckCounter(DealerHand)
        else:
            DealerPlay(DealerHand, ResultsDict, DeckOfCards)
    return ResultsDict

#Determines the winner and their payout.
def GameEnd(NameDict):
    Results=PlayGame()
    ResultsDict={}
    BlackJackList=Results['BlackJack']
    WinnerList=[]
    TieList=[]
    LossList=[]
    Winnings=0
    if Results[Name]>Results["Dealer"]:
        WinnerList.append(Name)
        NameDict[Name]+=bet
        Winnings+=bet
    elif Results[Name]==Results["Dealer"]:
        TieList.append(Name)
    else:
        LossList.append({Name})
        NameDict[Name]-=bet
        Winnings-=bet
    if 'PlayerSplit' in Results:
        if Results["PlayerSplit"] > Results["Dealer"]:
            WinnerList.append(Name)
            NameDict+=bet
            Winnings+=bet
        elif Results["PlayerSplit"] == Results["Dealer"]:
            TieList.append(Name)
        else:
            LossList.append({Name})
            NameDict[Name]-=bet
            Winnings-=bet
    if 'P2' in Results:
        if Results["P2"] > Results["Dealer"]:
            WinnerList.append('the computer')
        elif Results["P2"] == Results["Dealer"]:
            TieList.append('the computer')
        else:
            LossList.append({'the computer'})
    if 'P2Split' in Results:
        if Results["P2Split"] > Results["Dealer"]:
            WinnerList.append('the computer')
        elif Results["P2Split"] == Results["Dealer"]:
            TieList.append('the computer')
        else:
            LossList.append({'the computer'})
    if len(WinnerList)==0 and len(TieList)==0:
        WinnerList.append('the dealer')
    if Name in BlackJackList:
        NameDict[Name]+=bet/2
        Winnings+=bet/2
    ResultsDict['Winner']=WinnerList
    ResultsDict['Tie']=TieList
    ResultsDict['Loss']=LossList
    ResultsDict['Winnings']=Winnings
    return ResultsDict

#######################################################################################
    if __name__ == "__main__":
       play_game()

# Gets the settings from the player.
Name=input("What is your name?\n")
TwoMode=input("Would you like to turn on two player mode?\n").capitalize()
while TwoMode!="Yes" and TwoMode!="No":
    print("Please respond with a yes or a no")
    TwoMode = input("Would you like to turn on two player mode?\n").capitalize()
#Asks for the bets and looks at a seperate file in order to save the data between sessions.
PlayAgain='Yes'
while PlayAgain=="Yes":
    NameDict={}
    with open('MoneyLog.txt') as Names:
        NameList=Names.readlines()
    for items in NameList:
        news=items.split(',')
        NameDict[news[0]]=float(news[1])

    if Name not in NameDict:
        NameDict[Name]=100
    print(f'You have {NameDict[Name]} dollars to bet')

    Love=True
    while Love:
        try:
            bet=float(input(("How much would you like to bet?\n")))
            if bet>NameDict[Name]:
                print("That number is more than the money in your account")
                print("Please respond with a lower number or Venmo me")
            else:
                break
        except:
            print("Please respond with a number, don't include a dollar sign or any special characters.")

#prints out the information for winners, tied, and losers.


    ResultDict=GameEnd(NameDict)

    if 'the dealer' in ResultDict["Winner"]:
        print("The dealer won")
    if Name in ResultDict["Winner"]:
        print(f'{Name} won')
    if 'the computer' in ResultDict["Winner"]:
        print("The computer won")
    if Name in ResultDict["Tie"]:
        print(f'{Name} tied')
    if 'the computer' in ResultDict["Tie"]:
        print('The computer tied')
    if Name in ResultDict["Loss"]:
        print(f'{Name} lost')
    if 'the computer' in ResultDict['Loss']:
        print('The computer lost')

    if ResultDict['Winnings']<0:
        print(f'{Name} lost {math.fabs(ResultDict['Winnings'])}')
    elif ResultDict['Winnings']==0:
        print(f'{Name} had no change in their account')
    else:
        print(f'{Name} won ${ResultDict['Winnings']:.2f}')
    print(f'{Name} now has {NameDict[Name]:.2f} dollars in their account')

    with open('MoneyLog.txt','w') as file:
        for name,money in NameDict.items():
            file.write(f'{name},{money:.2f}\n')
    PlayAgain=input("Do you want to play again?\n").capitalize()
    while PlayAgain!="Yes" and PlayAgain!='No':
        print("Please answer with a yes or a no")
        PlayAgain = input("Do you want to play again?\n").capitalize()