from suite import Suite
from card import Card
import random


class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]  # 构成52张牌
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)  # 通过random的shuffle函数进行随机乱序操作

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        return self.current < len(self.cards)


poker = Poker()
print(poker.cards)

poker.shuffle()
print(poker.cards)

if poker.has_next:
    print(poker.deal())
