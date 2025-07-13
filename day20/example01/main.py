"""
扑克游戏
以示例形式讲授面向对象编程的概念
"""
from poker import Poker
from player import Player

poker = Poker()
poker.shuffle()

players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
# 轮流为玩家发牌
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

# 整理每个玩家的手牌
for player in players:
    player.arrange()
    print(f'{player.name}: {player.cards}')
