"""
Craps赌博游戏
"""
import random

money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')

    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break

    # 用两个1到6均匀分布的随机数模拟骰子的点数
    first_point = random.randint(1, 6) + random.randint(1, 6)
    print(f'玩家摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print('玩家胜!\n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        while True:
            current_point = random.randint(1, 6) + random.randint(1, 6)
            print(f'玩家摇出了{current_point}点')
            if current_point == 7:
                print('庄家胜!\n')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家胜!\n')
                money += debt
                break

print('你破产了!')
