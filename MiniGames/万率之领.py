"""
创作团队：HarayamaRese
创作作品：万率之领

"""
import random
import time
ww=random.randint(1,17)
弓箭塔="弓箭塔"
加农炮="加农炮"
迫击炮="迫击炮"
火炮="火炮"
隐形炸弹="隐形炸弹"
def a():
        print("")    
def b():
        print("")
def c():
        print("")
def d():
        print("")
def 流星石():
        while True:
                print("系统提示:法术类卡牌，无需附魂")
                教程=input("请选择攻击的目标\n>")
                if 教程 in 新手教程可攻击列表:
                        print("流星石打爆了%s,收复程度一颗星"%教程)
                        break
                else:
                        print("请正确选择")
#随机部落名字
name=["w","qfd","as","味","按时吃","撒","俺现在","dfv","eg","干活","治疗","部落","啊放假就好"]
name_2=["分担分担","下次","帮","辅导班地方","霍建华","任天堂","贝多芬","45","sfs","SD","刚发的"]
yu=["别人","gh","e","h","888","989","54188","dfbg","fs"]
ron=random.choice(name)
er=random.choice(name_2)
tlist=[]
新手教程可攻击列表=[]
#列表
print('-'*40)
print('\t欢迎来到万率之领')
print('-'*40)
time.sleep(1.5)
print('请为自己的部落取名字')
role=input('>')
coins=100
coins_two=100
print("服务器消息:欢迎%s部落来到万率之领"%role)
time.sleep(1)
print("尊敬的首长，您目前的部落信誉是%s,部落有%s金币"%(coins,coins_two))
#选择：if
while True:
        d=input("是否进入新手教程？\n 1=好的，我想看看呢\n 2=算了，我是老手\n >")
        if d=="1":
                print("万率之领是一个塔防，经营融为一体的游戏，你需要通过经营来获得战斗机会以体验游戏")
                w=input("现在来体验一把，好嘛？\n 1=ok\n 2=不要！\n >")
                if w=="2":
                        print("不行，你必须参加，谁叫你选择了新手教程呢")
                else:
                        print("好了！开始了")
                weq=int(1)
                tlist.append(weq)
                print("哥布林部落是一个古老的种族,存在于这个世界很久了，但是作恶多端四处袭击村民\n首领,您奉命前来剿灭哥布林部落一些残存势力\n")
                time.sleep(1.2)
                print("您需要拿到手中的卡牌并合理运用，您可以在打出卡牌以后进行附魂，来行动您所打出的卡牌\n您的目标是攻破对方的大本营\n但是哥布林们在周围放了很多防御建筑,现在开始勘测")
                time.sleep(1.2)
                #添加可攻击列表
                新手教程可攻击列表.append(弓箭塔)
                新手教程可攻击列表.append(加农炮)
                print("这个哥布林势力放了:\n 弓箭塔\n 加农炮\n您可以攻击的目标为\n %s\n %s"%(弓箭塔,加农炮))
                time.sleep(1.5)
                print("目前您的卡牌有:\n 流星石\n 炮手\n 弓弩手\n 炸弹敢死小队")
                time.sleep(1.5)
                while True:
                        www=input("请选择您打出的卡牌(名字)\n系统提示:如果乱出,将会由系统随机出牌\n>")
                        if www=="流星石":
                                流星石()
                        else:
                                if ww==1:
                                        a()
                                elif ww==7 or 8 or 3 or 9 or 10:
                                        b()
                                elif ww==2 or 11 or 12:
                                        c()
                                else:
                                        d()
                        
        elif d=="2":
                print("好的")
                time.sleep(1.0)
                break
        else:
                print("首领，请您正确选择！")
def one():
        print("尊敬的%s部落的首长,欢迎来到我的店铺，请您选尽情的选购"%role)
#循环插入
while True:
        s=input("首领，请选择您现在的操作:\n 1.商人的店铺\n 2.招募村民\n 3.远征\n 4.攻打哥布林部落\n 5.查看部落情况\n 6.退出\n >")
        if s=="1":
                one()
        elif s=="6":
                we=input("首领,您真的要退出吗\n 1=yes 2=no")
                if we=="1":
                        exit()
                else:
                        print("看吧，我说您不会退出的")
        else:
                print("首领，请您正确选择")