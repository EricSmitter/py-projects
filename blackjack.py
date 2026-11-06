import random
import os
import time

#The "deck" dictionary gets update throughout gameplay
deck = {'AC':11, 	'2C':2, 	'3C':3, 	'4C':4, 	'5C':5, 	'6C':6, 	'7C':7, 	'8C':8, 	'9C':9, 	'TC':10, 	'JC':10, 	'QC':10, 	'KC':10, 	'AS':11, 	'2S':2, 	'3S':3, 	'4S':4, 	'5S':5, 	'6S':6, 	'7S':7, 	'8S':8, 	'9S':9, 	'TS':10, 	'JS':10, 	'QS':10, 	'KS':10, 	'AD':11, 	'2D':2, 	'3D':3, 	'4D':4, 	'5D':5, 	'6D':6, 	'7D':7, 	'8D':8, 	'9D':9, 	'TD':10, 	'JD':10, 	'QD':10, 	'KD':10, 	'AH':11, 	'2H':2, 	'3H':3, 	'4H':4, 	'5H':5, 	'6H':6, 	'7H':7, 	'8H':8, 	'9H':9, 	'TH':10, 	'JH':10, 	'QH':10, 	'KH':10}
#This is a static dictionary to be able to map ranks to values even after they're gone from the deck
rank_vals = {'A':11, 	'2':2, 	'3':3, 	'4':4, 	'5':5, 	'6':6, 	'7':7, 	'8':8, 	'9':9, 	'T':10, 	'J':10, 	'Q':10, 	'K':10, 	'A':1, 	'2':2, 	'3':3, 	'4':4, 	'5':5, 	'6':6, 	'7':7, 	'8':8, 	'9':9, 	'T':10, 	'J':10, 	'Q':10, 	'K':10}


class hand: #This class handles both dealer and player hands
    def __init__(self, name): #initialize with empty dictionary and a name variable
        self.cards = {}
        self.name = name
    def draw(self, deck): #player/dealer add a card to their hand
        if len(deck) >= 1: #We'll put this whole function inside a check that the deck still
            card = random.choice(list(deck)) #Draw a card from the deck
            self.cards[card] = deck[card] #Add that card to the players hand
            if card[0] == "A": #Check if the card is an ace
                if self.hand_val() > 21: #If the ace pushes the total hand value over 21,
                    self.cards[card] = 1 #Change it's value to a 1
            del deck[card] #Remove that card from the deck
            return card
        else: #If there are no more cards, we'll break out of the program.
            clear_screen()
            print("Error: Deck is empty!")
            return
    def hand_val(self): #We want a method to calculate the value of the hand
        val = 0
        for c in self.cards:
            val += self.cards[c]
        return val
    def is_bust(self): #This method checks if hand_val() is over 21
        value = self.hand_val()
        is_bust = False
        if value > 21:
            is_bust = True
        return is_bust
    def is_blackjack(self): #This method checks if hand_val() is equal to 21
        value = self.hand_val()
        is_blackjack = False
        if value == 21:
            is_blackjack = True
        return is_blackjack

def clear_screen(): #Helper function to clear the output.
    os.system('cls' if os.name == 'nt' else 'clear')

#Generic turn function that detects a dealer/player hand
def turn(person):
    if person.name == "Dealer": #If it is the dealer's turn, they hit under 17
        if len(deck) != 0:
            while person.is_bust() == False and len(deck) !=0:
                dealing(1)
                card_print(person,*hand_unpack(person)) #Show the cards again
                if person.hand_val() < 17: #The dealer draws on anything less than 17
                    print("\nDealer Draws")
                    person.draw(deck)
                    person.hand_val() #Every draw, run hand_val
                else:
                    print("\nDealer Stands") #if the dealer has a hand less than 17, they stand
                    break
            else:
                if len(deck) == 0:
                    print("Oops! Out of cards")
                else:
                    pass
        else:
            print("Oops! Out of cards")
    else:
        #choice = "hit" #Initiate the choice with a default
        if len(deck) != 0:
            while person.is_bust() == False and len(deck) !=0:
                choice = input("Would you like to hit or stand? ")
                if choice == "hit": #We'll continue the draw.
                    dealing(1)
                    person.draw(deck)
                    person.hand_val()
                    card_print(person,*hand_unpack(person))
                if choice == "stand":
                    break
        else:
            print("Oops! Out of cards.")


def game_check(dealer, player):
    if len(deck) > 0:
        clear_screen()
        dealing(2)
        card_print(dealer,*hand_unpack(dealer)) #Pass the full player/dealer object and call their name where needed.
        card_print(player,*hand_unpack(player))
        p_val = player.hand_val()
        d_val = dealer.hand_val()
        print("\n===============")
        if player.is_bust():
            print("Player has busted. The house wins again..")
        elif dealer.is_bust():
            print("Dealer has busted! YOU WIN!")
        elif player.is_blackjack():
            print("Player has blackjack! YOU WIN!")
        elif dealer.is_blackjack():
            print("Dealer has blackjack, the house wins again...")
        else:
            if p_val > d_val:
                print(f"Player Wins!")
            elif d_val > p_val:
                print(f"Dealer wins!")
            elif p_val == d_val:
                print(f"It's a tie!")
        print(f"\n Player: {p_val}\n Dealer: {d_val}")
    else:
        pass


#Helper function to unpack hands into their suits and ranks
def hand_unpack(person):
    suit = list()
    rank = list()
    for k,v in person.cards.items():
        suit.append(k[0])
        rank.append(k[1])
    return suit, rank

#This function takes the person and the unpacked rank and suit from the hand_unpack helper function and prints ascii drawn cards
def card_print(person, rank, suit):
    suit_ascii = {"C":"\u2663", "H":"\u2665", "D":"\u2666", "S":"\u2660"} #Define suit keys as ascii characters for hearts, clubs etc
    suit_section = "" #Blank strings to append later
    rank_section = ""
    top = "  _____   " #Create top/bottom sections of the card to print
    bottom = " |_____|  "
    if person.name == "Dealer": #For the dealer we only want to show their second card.
        print(f"\n{person.name} is showing {person.hand_val()}")
        for s in suit:
            s_ascii = suit_ascii[s] #Map the suit to it's ascii character
            suit_section += f" |  {s_ascii}  |  "
        for r in rank: #Build the rank section string
            if r == "T": #10 is our special case, i've mapped it to "T" to keep it to a single char for id
                r = "10"
                rank_section += f" | {r}  |  " #Map T back to 10 and update the string accordingly.
            else:
                rank_section += f" |  {r}  |  "
        print(f"{top * len(suit)}\n{rank_section}\n{suit_section}\n{bottom * len(suit)}") #Print out the cards
#        print(f"The dealer is showing {rank_vals[rank[1]]}")
#        top = " _ _____"
#        bottom = "|_|_____|"
#        if rank[1] == "T":
#            rank_section = f"| | 10  |"
#        else:
#            rank_section = f"| |  {rank[1]}  |"
#        suit_section = f"| |  {suit_ascii[suit[1]]}  |"
#        print(f"{top}\n{rank_section}\n{suit_section}\n{bottom}")
    else: #The else case is for the player, and we can change the dealer name later to show their full hand
        print(f"\n{person.name} is showing {person.hand_val()}")
        for s in suit:
            s_ascii = suit_ascii[s] #Map the suit to it's ascii character
            suit_section += f" |  {s_ascii}  |  "
        for r in rank: #Build the rank section string
            if r == "T": #10 is our special case, i've mapped it to "T" to keep it to a single char for id
                r = "10"
                rank_section += f" | {r}  |  " #Map T back to 10 and update the string accordingly.
            else:
                rank_section += f" |  {r}  |  "
        print(f"{top * len(suit)}\n{rank_section}\n{suit_section}\n{bottom * len(suit)}") #Print out the cards

#A function to add a little breather between turns/operations
def dealing(x): #x tells the function how many loops to do
    suit_ascii = {"C":"\u2663", "H":"\u2665", "D":"\u2666", "S":"\u2660"}
    output = ""
    for i in range(x): #The loop adds another char and returns to the start of that line
        for c in suit_ascii:
            print(f"\r{output}", end=" ", flush=True)
            output += f" {suit_ascii[c]}"
            time.sleep(0.2)


def main():
    play_again = "y"
    while play_again == "y" and len(deck) > 4:
        print("Welcome to Python Blackjack!")
        dealing(2)
        player = hand("Player") #Create player object
        dealer = hand("Dealer") #Create dealer object
        for i in range(2): #Deal two cards initially
            player.draw(deck)
            dealer.draw(deck)
        card_print(dealer,*hand_unpack(dealer)) #Pass the full player/dealer object and call their name where needed.
        card_print(player,*hand_unpack(player))
        turn(player)
        if player.is_bust():
            game_check(dealer, player)
        else:
            turn(dealer)
            game_check(dealer, player)
        play_again = input("Play again? y/n ")
        clear_screen()
    if len(deck) <= 4:
        print("Looks like we're out of cards. Come again soon!")
main()
