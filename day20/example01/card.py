from suite import Suite


class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        """
        __repr__ 魔法方法的作用其实类似于 __str__ 魔法方法，是一种官方说明方法。
        换句话说，__repr__ 偏向展示给开发人员，__str__ 偏向展示给用户
        """
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        """
        自定义排序
        在玩家整理手牌时需要进行排序，只要自定义该魔法方法即可
        """
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value


card1 = Card(Suite.SPADE, 1)
card2 = Card(Suite.DIAMOND, 12)
print(card1)
print(card2)
