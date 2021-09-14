import random

# create three global variable as tuple
suits = ('Diamonds', 'Hearts', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """Card class contains the attributes such as suit(diamond, spade,), integer value of the card and the
    rank of the card
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    # Instantiating 52 card objects in a deck
    def __init__(self):
        self.card_obj_list = []
        for suit in suits:  # for each suit
            for rank in ranks:  # for each rank
                # Card object is added to the list
                self.card_obj_list.append(Card(suit, rank))

    # shuffle the 52 cards in a deck
    def shuffle_deck(self):
        random.shuffle(self.card_obj_list)

    # Need to remove a card from the 52 deck cards
    def deal_one(self):
        return self.card_obj_list.pop()


class Player:
    # Player should have a name and a deck of cards
    def __init__(self, name, score=0):
        self.name = name
        self.card_obj_list = []
        self.score = score

    # return a string when a print() is called
    def __str__(self):
        return f"{self.name} has {len(self.card_obj_list)} no of cards."

    # Player is able to remove the top card from his deck
    def remove_one_card(self):
        return self.card_obj_list.pop(0)

    # Player should be able to add a single card or multiple cards
    def add_cards(self, card_objects):
        # Add multiple cards/list of cards at the bottom of stack(right most of a list)
        if isinstance(card_objects, type([])):
            self.card_obj_list.extend(card_objects)
        else:
            self.card_obj_list.append(card_objects)


# GAME SETUP
def game_logic():
    players = []
    for i in range(1, 3):
        player_name = input("Please enter the name of player " + str(i) + ":")
        players.append(Player(player_name))

    deck_object = Deck()
    # Shuffle the 52 cards(objects)
    deck_object.shuffle_deck()

    # Split the deck into halves between two players(each 26)
    for i in range(26):
        players[0].add_cards(deck_object.deal_one())
        players[1].add_cards(deck_object.deal_one())
    print()
    print(players[0])
    print(players[1])

    # Game Logic/Playing
    game_on = True
    round_num = 0
    while game_on:
        print("\t Welcome to the Card War Game!")

        round_num += 1
        print("Round: ", round_num)

        # Check if the player has zero cards, then he/she lost the game
        if len(players[0].card_obj_list) == 0:
            print(players[1].name, " has won the war game!")
            game_on = False
            break

        if len(players[1].card_obj_list) == 0:
            print(players[0].name, " has won the war game!")
            game_on = False
            break

        # A New Round begins and player1_card_on_table would be empty
        # reset each players cards list on the table

        # Remove a card object from deck of player one and put it face up on the table
        player1_card_ontable = []
        player1_card_ontable.append(players[0].remove_one_card())

        # Remove a card object from deck of player two and put it face up on the table
        player2_card_ontable = []
        player2_card_ontable.append(players[1].remove_one_card())

        # Compare the cards on the table, Assuming the war is on
        at_war = True
        while at_war:
            print("Compare the card values:")
            print(players[0].name, ':', player1_card_ontable[-1], player1_card_ontable[-1].value)
            print(players[1].name, ':', player2_card_ontable[-1], player2_card_ontable[-1].value)
            if player1_card_ontable[-1].value > player2_card_ontable[-1].value:
                players[0].add_cards(player1_card_ontable)
                players[0].add_cards(player2_card_ontable)
                print(players[0].name, "has won both the cards")
                print("\n\tStatistics:")
                print(players[0].name, " - ", len(players[0].card_obj_list))
                print(players[1].name, " - ", len(players[1].card_obj_list))
                at_war = False

            elif player1_card_ontable[-1].value < player2_card_ontable[-1].value:
                players[1].add_cards(player1_card_ontable)
                players[1].add_cards(player2_card_ontable)
                print(players[1].name, "has won both the cards")
                print("\n\tStatistics:")
                print(players[0].name, " - ", len(players[0].card_obj_list))
                print(players[1].name, " - ", len(players[1].card_obj_list))
                at_war = False

            else:
                print('\t \t WAR!')
                # check if the player has enough card(here min 5 cards) to play the war
                if len(players[0].card_obj_list) < 5:
                    print(players[0].name, ' does not have enough cards to play war')
                    print(players[1], ' wins!')
                    game_on = False
                    break

                elif len(players[1].card_obj_list) < 5:
                    print(players[1], ' does not have enough cards to play war')
                    print(players[0], ' wins!')
                    game_on = False
                    break
                else:
                    for i in range(5):
                        # Player1 and Player2 are discarding 5 cards from their cards (card_obj_list)
                        player1_card_ontable.append(players[0].remove_one_card())
                        player2_card_ontable.append(players[1].remove_one_card())


if __name__ == '__main__':
    game_logic()
