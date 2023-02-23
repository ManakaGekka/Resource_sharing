import random
 
 
class Dog(object):
    def __init__(self, name):
        self._name = name
        self._hp = 50
        self._attack = 20
 
    @property
    def name(self):
        return self._name
 
    @property
    def hp(self):
        return self._hp
 
    @property
    def attack(self):
        return self._attack
 
    @hp.setter
    def hp(self, hp):
        self._hp = hp
 
    def attack_dog(self, dog):
        dog.hp -= self._attack
 
 
class Player(object):
    def __init__(self, name):
        self._name = name
        self._hp = 100
        self._dogs = []
 
    @property
    def name(self):
        return self._name
 
    @property
    def hp(self):
        return self._hp
 
    @hp.setter
    def hp(self, hp):
        self._hp = hp
 
    def add_dog(self, dog):
        self._dogs.append(dog)
 
    def attack_dog(self, dog):
        pass
 
    def attack_dog_with_random_dog(self, dog):
        random_dog = random.choice(self._dogs)
        random_dog.attack_dog(dog)
        print("{}用{}攻击了{}，{}受到{}点伤害".format(
            self._name, random_dog.name, dog.name, dog.name, random_dog.attack))
 
 
def main():
    # 先创建2个玩家
    print("------游戏开始------")
    p1 = Player("风清扬")
    p2 = Player("丁春秋")
 
    # p1添加4只狗
    p1.add_dog(Dog("旺财"))
    p1.add_dog(Dog("二毛"))
    p1.add_dog(Dog("骨头"))
    p1.add_dog(Dog("大毛"))
 
    # p2添加2只狗
    p2.add_dog(Dog("铁憨憨"))
    p2.add_dog(Dog("花花"))
 
    round = 1
    while p1.hp > 0 and p2.hp > 0:
        print("------第{}回合------".format(round))
        # p1的狗攻击p2
        p1.attack_dog_with_random_dog(p2)
        # p2的狗攻击p1
        p2.attack_dog_with_random_dog(p1)
        print("{}还剩下{}点血".format(p1.name, p1.hp))
        print("{}还剩下{}点血".format(p2.name, p2.hp))
        round += 1
    if p1.hp > 0:
        print("{}赢了！".format(p1.name))
    else:
        print("{}赢了！".format(p2.name))
 
 
if __name__ == '__main__':
    main()
