import random

# Declare the global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': (1, 11)}
playing = True


# card class holds suit and rank attribute for each object class
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    # string representation of card object
    def __str__(self):
        return f"{self.rank} of {self.suit}"  # 'has value' + 'str(self.value)'


class Deck:
    # The deck is a list of card objects
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    # it returns the name of all the cards in the deck list
    def __str__(self):
        deck_comp = ''
        # item represents a card object
        for item in self.deck:
            deck_comp += '\n' + item.__str__()  # item.str return the name of the single card
        return 'The deck has: ' + deck_comp

    # it shuffles the card objects in the deck list
    def shuffle_deck(self):
        random.shuffle(self.deck)

    # it removes one card object from the deck list
    def deal(self):
        return self.deck.pop(0)


class Hand:
    # card object in someone's hand (computer/player)
    def __init__(self):
        self.cards = []
        self.hand_val = 0
        self.aces = 0

    def add_card(self, card):
        # card will come from the deck.deal() and will pass as an argument to this method
        self.cards.append(card)
        self.hand_val += card.value
        # track the number of aces(how many aces they got)
        if card.rank == 'Ace':
            self.aces += 1
        # return self.hand_val

    def adjust_for_ace(self):
        # If the total value > 21 and after hit i got an ace, then change the
        # ace value to 1 in stead of 11
        if self.hand_val > 21 and self.aces > 0:
            self.hand_val -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# This method asks user input for the chips and raise exception if it is string value
def make_bet(player_chips):
    do_bet = False
    while not do_bet:
        try:
            player_chips.bet = int(input("How many chips you want to bet? "))
            if isinstance(player_chips, type(1)):
                do_bet = True
        except ValueError:
            print('Whoops! please enter an integer')
        else:
            if player_chips.bet > player_chips.total:
                print('You cannot bet amount greater than total amount', player_chips.total)
            else:
                do_bet = True


# this function take a card from deck and give that to the player's hand
# Also adjust the value of the Ace if the player has an ace card
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# This function asks players to stay or hit  and tales deck and hand as argument
def hit_or_stay(deck, hand):
    global playing
    while True:
        try:
            x = input("Would you like to Hit or Stand? Enter 'H' or 'S': ")
            if x not in ['h', 's']:
                raise Exception
        except Exception:
            print('Whoops!! Please enter between H and S')
        else:
            if x.upper() == 'H':
                hit(deck, hand)
                break
            if x.upper() == 'S':
                print('Player stands and dealer is playing')
                playing = False
                break


def show_some(player, dealer):
    # show only one card of dealer and the value
    print("\\n The Dealer's Hand: ")
    print("The First Card is hidden!")
    print(dealer.cards[1])  # as the 1st card is hidden

    # shows 2 cards of player's card and the value of cards
    print("\\n The player's Hand: ")
    for card in player.cards:
        print(card)
    print("The value of the player's hand: ", player.hand_val)


def show_all(player, dealer):
    # show all the cards of dealer and the total card value
    dealer_sum = 0
    print("\\n Dealer's full hand: ")
    for card in dealer.cards:
        print(card)
    print("The value of the dealer's hand: ", dealer.hand_val)

    # show all the cards of player and total card value
    player_sum = 0
    print("\\n Player's full hand: ")
    for card in player.cards:
        print(card)
    print("The value of the player's hand: ", player.hand_val)


def player_bust(player, dealer, chips):
    print("The Player is busted!")
    chips.lose_bet()


def player_win(player, dealer, chips):
    print("The Player is Winner!")
    chips.win_bet()


def dealer_bust(player, dealer, chips):
    print("The Dealer is busted")
    chips.lose_bet()


def dealer_win(player, dealer, chips):
    print("The Dealer is busted")
    chips.lose_bet()


def push(player, dealer):
    print("The player and dealer have both 21, PUSH")


while True:
    # Print an opening statement
    print("THE GAME BEGINS")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle_deck()

    player = Hand()
    dealer = Hand()
    for i in range(2):
        c1 = deck.deal()
        player.add_card(c1)
    for i in range(2):
        c2 = deck.deal()
        dealer.add_card(c2)

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    make_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stay(deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.hand_val > 21:
            player_bust(player, dealer, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.hand_val <= 21:
        while dealer.hand_val < 17:
            hit_or_stay(deck, dealer)

        # Show all cards
        show_all(player, dealer)

        # Run different winning scenarios
        if dealer.hand_val > 21:
            dealer_bust(player, dealer, player_chips)
        elif dealer.hand_val > player.hand_val:
            dealer_win(player, dealer, player_chips)
        elif dealer.hand_val < player.hand_val:
            player_win(player, dealer, player_chips)
        else:
            push(player, dealer)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at",player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break


