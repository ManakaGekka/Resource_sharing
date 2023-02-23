import time, random

class Role():
    def __init__(self,name = '|角色|'):
        self.name = name
        self.life = random.randint(100,150)
        self.attack = random.randint(30,50)

class Sains_knight(Role):
    def __init__(self,name = '|圣光骑士|'):
        Role.__init__(self,name)
        self.life = 5 * self.life
        self.attack = 3 * self.attack

    def fight_buff(self,enemy):
        if enemy == '|暗影刺客|':
            self.attack *= 1.5
        else:
            self.attack = self.attack

class Shadow_Assassin(Role):
    def __init__(self,name = '|暗影刺客|'):
        Role.__init__(self, name)
        self.life = 3 * self.life
        self.attack = 5 * self.attack

    def fight_buff(self,enemy):
        if enemy == '|精灵弩手|':
            self.attack *= 1.5
        else:
            self.attack = self.attack

class Faerie_Bowman(Role):
    def __init__(self,name = '|精灵弩手|'):
        Role.__init__(self, name)
        self.life = 4 * self.life
        self.attack = 4 * self.attack

    def fight_buff(self,enemy):
        if enemy == '|圣光骑士|':
            self.attack *= 1.5
        else:
            self.attack = self.attack

class GAME():
    def __init__(self):
        self.players = []
        self.enemies = []
        self.show_title()
        self.show_role()
        self.order_role()
        self.pk_role()

    # 随机生成角色的属性
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Sains_knight(),Shadow_Assassin(),Faerie_Bowman()]))
            self.enemies.append(random.choice([Sains_knight(),Shadow_Assassin(),Faerie_Bowman()]))

    # 生成和展示角色信息
    def show_role(self):
        self.born_role()
        # 展示我方的3个角色
        print('----------------- 角色信息 -----------------')
        print('你的队伍：')
        for i in range(3):
            print('|我方|%s  血量：%s  攻击：%s'
                  % (self.players[i].name,self.players[i].life,self.players[i].attack))
        print('--------------------------------------------')
        print('敌人队伍：')

        # 展示敌方的3个角色
        for i in range(3):
            print('|敌方|%s  血量：%s  攻击：%s'
                  % (self.enemies[i].name, self.enemies[i].life, self.enemies[i].attack))
        print('--------------------------------------------')
        input('请按回车键继续。')  # 为了让玩家更有控制感，可以插入类似的代码来切分游戏进程。

    # 角色排序，选择出场顺序。
    def order_role(self):
        order_dict = {}
        for i in range(3):
            order = int(input('你想让{}第几个上场？（输入数字1-3）'.format(self.players[i].name)))
            order_dict[order] = self.players[i]

        self.players = []
        for i in range(1,4):
            self.players.append(order_dict[i])

        print('\n我方角色的出场顺序是：%s、%s、%s' % (self.players[0].name, self.players[1].name, self.players[2].name))
        print('敌方角色的出场顺序是：%s、%s、%s' % (self.enemies[0].name, self.enemies[1].name, self.enemies[2].name))

    # 角色PK
    def pk_role(self):
        round = 1
        score = 0
        for i in range(3):  # 一共要打三局
            player_name = self.players[i].name
            enemy_name = self.enemies[i].name
            #判断敌人是否对其有克制效果，有则进行攻击加成
            self.players[i].fight_buff(enemy_name)
            self.enemies[i].fight_buff(player_name)
            player_life = self.players[i].life
            player_attack = self.players[i].attack
            enemy_life = self.enemies[i].life
            enemy_attack = self.enemies[i].attack

            # 每一局开战前展示战斗信息
            print('\n----------------- 【第%s局】 -----------------' % round)
            print('玩家角色：%s vs 敌方角色：%s ' % (player_name, enemy_name))
            print('%s 血量：%s  攻击：%s' % (player_name, player_life, player_attack))
            print('%s 血量：%s  攻击：%s' % (enemy_name, enemy_life, enemy_attack))
            print('--------------------------------------------')
            input('请按回车键继续。\n')

            # 开始判断血量是否都大于零，然后互扣血量。
            while player_life > 0 and enemy_life > 0:
                enemy_life = enemy_life - player_attack
                player_life = player_life - enemy_attack
                print('%s发起了攻击，%s剩余血量%s' % (player_name, enemy_name, enemy_life))
                print('%s发起了攻击，%s剩余血量%s' % (enemy_name, player_name, player_life))
                print('--------------------------------------------')
                time.sleep(1)
            else:  # 每局的战果展示，以及分数score和局数的变化。
                # 调用show_result()函数，打印返回元组中的result。
                print(self.show_result(player_life,enemy_life)[1])
                # 调用show_result()函数，完成计分变动。
                score += int(self.show_result(player_life,enemy_life)[0])
                round += 1
        input('\n点击回车，查看比赛的最终结果\n')

        if score > 0:
            print('【最终结果：你赢了！】\n')
        elif score < 0:
            print('【最终结果：你输了！】\n')
        else:
            print('【最终结果：平局！】\n')

    # 返回单局战果和计分法所加分数。
    def show_result(self,player_life, enemy_life):  # 注意：该函数要设定参数，才能判断单局战果。
        if player_life > 0 and enemy_life <= 0:
            result = '\n敌人死翘翘了，你赢了！'
            return 1, result  # 返回元组(1,'\n敌人死翘翘了，你赢了！')，类似角色属性的传递。
        elif player_life <= 0 and enemy_life > 0:
            result = '\n悲催，敌人把你干掉了！'
            return -1, result
        else:
            result = '\n哎呀，你和敌人同归于尽了！'
            return 0, result
    #展示标题
    def show_title(self):
        print('''--------------欢迎来到炼狱角斗场-----------------
在昔日的黄昏山脉，陆奥帝国的北境边界上，有传说中的‘炼狱角斗场'!
鲜血与战斗是角斗士的归宿，金钱与荣耀是角斗士的信仰！
今日，只要【你的队伍】能取得胜利，你将获得一笔够花500的财富!
将随机生成【你的队伍】和【敌人队伍】！''')
        input('\n狭路相逢勇者胜，话不投机半句多(按任意键继续...)')

GAME_START = GAME()
