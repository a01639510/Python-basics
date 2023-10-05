import random

player_cards = []
table_cards = []
repeated_cards =[]
correct_cards= []
cards =('The rooster', 'The devil', 'The lady', 'The catrín', 'The umbrella', 'The mermaid', 'The ladder', 'The bottle', 'The barrel', 'The tree', 'The melon', 'The brave', 'The little cap', 'Death', 'The pear', 'The flag', 'The bandolon', 'The cello', 'The heron', 'The bird', 'The hand', 'The boot', 'The moon', 'The parrot', 'The drunkard', 'The black boy', 'The heart', 'The watermelon', 'The drum', 'The shrimp')
win = False

#this function defines the 9 random cards that the player will have to guess correctly
def game_cards():
    #Gives 9 random cards to the player
    x = 0
    while x < 9:
        card_num = random.randint(1,30)
        player_cards.append(cards[card_num -1 ])
        x = x+1
    print(player_cards)
#validates if the player won or not
def validation():
    global win
    if len(correct_cards) > 8:
        print("\n \n \n \n \n LOTTERY! \n\n")
        win = True
    else:
        print("some cards had not been passed")
        win = False
#this function performs the game cycle
def game():
    #make the variable win a global variable and not a local one
    global win
    while win == False:

        card_num = random.randint(1,30)
        #validate if the letter has already gone out
        if card_num in repeated_cards:
            print("repeated output")
            
        else:
            #Adds the card to the validation of repeated cards, the cards that have been drawn and the card of the turn
            table_cards.append(cards[card_num -1 ])
            print (cards[card_num -1 ])
            repeated_cards.append(card_num)
            turn_card = (cards[card_num -1 ])
            #Validates if the card is in the player's game
            if turn_card in player_cards:
                correct_cards.append(card_num)

            
        #Input to know if the player thinks he already won
        lottery = input("write lottery when you have won >>>>")
        if lottery == "lottery" or lottery == "Lottery":
        
            validation()
            lottery = ""

#execute the code
game_cards()
game()