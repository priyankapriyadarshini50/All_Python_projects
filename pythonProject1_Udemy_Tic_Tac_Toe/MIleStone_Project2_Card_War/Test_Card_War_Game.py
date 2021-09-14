import unittest
from Card_War_Game import Card, Deck


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card('Diamonds', 'Four')
        self.card_2 = Card('Spades', 'Queen')

    def tearDown(self):
        print('Test execution completed')

    def test_object(self):
        self.assertEqual(self.card_1.__str__(), 'Four of Diamonds')
        self.assertEqual(self.card_2.__str__(), 'Queen of Spades')


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck_1 = Deck()
        self.deck_2 = Deck()

    def tearDown(self):
        print('Test execution completed')

    def test_shuffle_deck(self):
        self.assertNotEqual(self.deck_1.shuffle_deck(), self.deck_1.card_obj_list)
        self.assertNotEqual(self.deck_2.shuffle_deck(), self.deck_2.card_obj_list)


if __name__ == '__main__':
    unittest.main()
