import unittest

from InnerFunction import *


class TestInner(unittest.TestCase):
    # intToStringCard 확인
    def testintToStringCard(self):
        card = [0]
        self.assertEqual(intToStringCard(card)[0], 'spadesA')

    # count 확인
    def testCount(self):
        card = [7, 42]
        self.assertEqual(count(card), 12)

    # blackjack 확인
    def testBlackJack(self):
        card = [0, 50]
        self.assertEqual(blackjack(card), True)

        card = [0, 1]
        self.assertEqual(blackjack(card), False)

    # burst 확인
    def testBurst(self):
        card = [4, 10, 23]
        self.assertEqual(burst(card), True)

        card = [4, 10]
        self.assertEqual(burst(card), False)

    # fight 확인
    def testFight(self):
        self.assertEqual(fight(19, 20), 0)
        self.assertEqual(fight(19, 19), 2)
        self.assertEqual(fight(19, 18), 1)

    #

if __name__ == '__main__':
    unittest.main()

marks = ['spades', 'diamonds', 'hearts', 'clubs']
card_english = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
