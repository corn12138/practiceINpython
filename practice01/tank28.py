'''
    音效处理
'''
import pygame
from time import sleep
import random
from pygame.sprite import collide_rect # 碰撞检测
#设置通用属性
BG_COLOR = pygame.Color(0,0,0) # 设置窗口背景颜色
SCREEN_WIDTH = 800  # 设置窗口的宽度
SCREEN_HEIGHT = 600 # 设置窗口的高度
TEXT_COLOR = pygame.Color(255,0,0) # 设置文字颜色

class Tank:
    """
    坦克类
    """
    def __init__(self) -> None:
        self.image = None
        self.live = True
        #记录坦克 原来的位置
        self.old_left = 0
        self.old_top = 0

    def display_tank(self) -> None:
        """
        坦克显示
        """
        #获取最新坦克朝向的图片
        self.image = self.images.get(self.direction)
        #绘制坦克
        MainGame.window.blit(self.image,self.rect)
    def move(self) -> None:
        """
        坦克移动
        """
        #移动前记录坦克的坐标
        self.old_left = self.rect.left
        self.old_top = self.rect.top
        #判断坦克的方向，进行移动
        if self.direction == 'L':
            # 判断坦克是否在左边界
            if self.rect.left > 0:
                self.rect.left -= self.speed

        elif self.direction == 'R':
            # 判断坦克是否在右边界
            if self.rect.right < SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            # 判断坦克是否在上边界
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            # 判断坦克是否在下边界
            if self.rect.bottom < SCREEN_HEIGHT:
                self.rect.top += self.speed
    def shot(self) -> None:
        """
        坦克射击
        """
        pass
    def tank_hit_wall(self):
        """
        坦克撞墙
        """
        for wall in MainGame.wall_list:
            # 检测当前坦克是否与墙壁发生碰撞,如果碰撞，将坦克移的位置还原
            if pygame.sprite.collide_rect(self,wall):
                # self.rect.left = self.old_left
                # self.rect.top = self.old_top
                self.componets()
    def tank_collide_tank(self,tank):
        """
        坦克与坦克碰撞,
        """
        if pygame.sprite.collide_rect(self,tank):
            #
            if self and tank and self.live and tank.live:
                # self.rect.left = self.old_left
                # self.rect.top = self.old_top
                self.componets()
    # 抽出的方法
    def componets(self):
        self.rect.left = self.old_left
        self.rect.top = self.old_top


class MyTank(Tank):
    """
    我方坦克
    """
    def __init__(self,left,top) -> None:
        super(MyTank,self).__init__() # 调用父类的初始化方法
        # 设置我方tank的图片
        self.images = {
            'U':pygame.image.load('img/p1tankU.gif'), # 上
            'D':pygame.image.load('img/p1tankD.gif'), # 下
            'L':pygame.image.load('img/p1tankL.gif'), # 左
            'R':pygame.image.load('img/p1tankR.gif')  # 右
        }
        # 方向
        self.direction = 'L'
        # 根据当前图片的方向获取图片
        self.image = self.images.get(self.direction)
        #获取图片的区域
        self.rect = self.image.get_rect()
        #设置坦克的位置
        self.rect.left = left
        self.rect.top = top

        #设置移动的速度
        self.speed = 10

        #坦克移动的开关,false表示不移动,True表示移动
        self.remove = False

class EnemyTank(Tank):
    """
    敌方坦克
    """
    def __init__(self,left,top,speed) -> None:
        super(EnemyTank,self).__init__() # 调用父类的初始化方法
        self.images = {
            'U':pygame.image.load('img/enemy1U.gif'), # 上
            'D':pygame.image.load('img/enemy1D.gif'), # 下
            'L':pygame.image.load('img/enemy1L.gif'), # 左
            'R':pygame.image.load('img/enemy1R.gif')  # 右
        }
        # 设置敌方tank的方向
        self.direction = self.rand_direction()
        # 根据当前图片的方向获取图片
        self.image = self.images.get(self.direction)
        #获取图片的区域
        self.rect = self.image.get_rect()
        #设置坦克的位置
        self.rect.left = left
        self.rect.top = top
        #设置移动的速度
        self.speed = speed

        #设置移动的步长
        self.step = 20

    def rand_direction(self) -> str:
        """
        生成随机方向
        """
        chice = random.randint(1,4)
        if chice == 1:
            return 'U'
        elif chice == 2:
            return 'D'
        elif chice == 3:
            return 'L'
        elif chice == 4:
            return 'R'

    def rand_move(self) -> None:
        """
        随机移动
        """
        # self.direction = self.rand_direction()
        # self.move()
        if self.step <= 0: # 步长为0时，重新生成随机方向
            self.direction = self.rand_direction()
            self.step = 20
        else:
            self.move()
            self.step -= 1 # 每移动一次，步长减1
    def shot(self):
        """
        敌方坦克子弹
        """
        # 随机生成一个数--作用是控制子弹的频率
        num = random.randint(1,100)

        if num < 5:
            return Bullet(self) # 创建子弹对象


class Bullet:
    """
    子弹类
    """
    def __init__(self,tank) -> None:
        #加载子弹图片
        self.image = pygame.image.load('img/enemymissile.gif')
        #获取子弹方向
        self.driction = tank.direction
        #获取子弹的图形
        self.rect = self.image.get_rect()
        #设置子弹的位置
        if self.driction =='L':
            self.rect.left = tank.rect.left - self.rect.width  # 子弹的left值 = 坦克的left值 - 子弹的宽度
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.height/2 # 子弹的top值 = 坦克的top值 + 坦克的宽度/2 - 子弹的高度/2
        elif self.driction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width # 子弹的left值 = 坦克的left值 + 坦克的宽度
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.height/2 # 子弹的top值 = 坦克的top值 + 坦克的宽度/2 - 子弹的高度/2
        elif self.driction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.driction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height

        #子弹的速度
        self.speed = 10
        #子弹的生存状态
        self.live = True

    def display_bullet(self) -> None:
        """
        子弹显示
        """
        MainGame.window.blit(self.image,self.rect) # 将子弹加入到窗口中
    def move(self) -> None:
        """
        子弹移动
        """
        # 根据子弹生成的方向，进行移动
        if self.driction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                #移除子弹
                self.live = False
        elif self.driction == 'R':
            if self.rect.left+self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False
        elif self.driction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
               self.live = False
        elif self.driction == 'D':
            if self.rect.top+self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False

    def hit_enemy_tank(self):
        """
        子弹击中敌方坦克
        """
        for enemy in MainGame.enemyTank_list:
            if collide_rect(self,enemy):
                #产生爆炸效果
                explode = Explode(enemy)
                #将爆炸效果加入到爆炸效果列表中
                MainGame.explode_list.append(explode)
                #修改子弹的状态
                self.live = False
                enemy.live = False

    def hit_my_tank(self):
        """
        子弹击中我方坦克
        """
        #判断我方坦克是否存活
        if MainGame.my_tank and MainGame.my_tank.live:
            #判断子弹是否击中我方坦克
            if collide_rect(self,MainGame.my_tank):
                #产生爆炸效果
                explode = Explode(MainGame.my_tank)
                #将爆炸效果加入到爆炸效果列表中
                MainGame.explode_list.append(explode)
                #修改子弹的状态
                self.live = False
                MainGame.my_tank.live = False
    def hit_wall(self):
        """
        子弹击中墙壁
        """
        for wall in MainGame.wall_list: # 遍历墙壁列表
            if collide_rect(self,wall):
                # 修改子弹的状态
                self.live = False
                # 修改墙壁的生命值
                wall.hp -= 1
                # 判断墙壁是否依然显示
                if wall.hp <= 0:
                    wall.live = False
                # 创建攻击音效对象
                music = Music('img/hit.wav')
                # 播放音效
                music.play_music()
class Wall:
    """
    墙壁类
    """
    def __init__(self,left,top) -> None:
        #加载墙壁的图片
        self.image = pygame.image.load('img/steels.gif')
        #获取墙壁的区域
        self.rect = self.image.get_rect()
        #设置墙壁的位置
        self.rect.left = left
        self.rect.top = top
        #设置墙壁的耐久值
        self.hp = 90
        # 设置墙壁的生存状态
        self.live = True
    def display_wall(self) -> None:
        """
        墙壁显示
        """
        MainGame.window.blit(self.image,self.rect)

class Explode:
    """
    爆炸效果类
    """
    def __init__(self,tank:Tank) -> None:
        #加载爆炸效果的图片
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif'),
        ]
        #爆炸效果的位置
        self.rect = tank.rect
        #爆炸效果的图片索引
        self.step = 0
        #获取渲染图像
        self.image = self.images[self.step]
        #爆炸效果的生存状态
        self.live = True # 爆炸效果存活
    def display_explode(self) -> None:
        """
        爆炸效果显示
        """
        if self.step < len(self.images): # 如果图片索引小于图片的数量
            #获取当前爆炸的效果的图片
            self.image = self.images[self.step]
            #获取下一张爆炸效果的图像的索引
            self.step += 1
            #绘制爆炸效果
            MainGame.window.blit(self.image,self.rect)
        else:
            #初始化爆炸效果的图片索引
            self.step = 0
            #修改爆炸效果的生存状态
            self.live = False # 爆炸效果消失

class Music:
    """
    音效类
    """
    pygame.mixer.init()
    def __init__(self,filename:str) -> None:
        #创建音乐文件
        pygame.mixer.music.load(filename)
    def play_music(self) -> None:
        """
        播放音效
        """
        pygame.mixer.music.play()

class MainGame:
    """
    游戏主窗口类
    """
    # 创建游戏窗口
    window = None
    #设置我方坦克
    my_tank = None
    #存储敌方坦克的列表
    enemyTank_list = []
    #敌方坦克的数量
    enemyTank_count = 6
    #存储我方子弹的列表
    my_bullet_list = []
    #存储敌方子弹的列表
    enemy_bullet_list = []
    #存储爆炸效果的列表
    explode_list = []
    #存储墙壁的列表
    wall_list = []
    def __init__(self) -> None:
        pass
    def start_game(self) -> None:
        """
        开始游戏
        :return:
        """
        #初始化游戏窗口
        pygame.display.init()
        #创建游戏窗口
        MainGame.window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        #设置窗口标题
        pygame.display.set_caption("坦克大战1.0")
        #创建我方坦克
        self.create_my_tank()
        #创建敌方坦克
        self.create_enemy_tank()
        #创建墙壁
        self.create_wall()
        #使窗口保持显示状态-刷新窗口
        while True:
            sleep(0.02) #每次休眠0.02s
            #给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            #增加提示文字
            # 1.变量增加文字内容
            # num = 6
            text = self.get_text_surface('敌方坦克剩余数量{0}'.format(len(MainGame.enemyTank_list)))
            # 2.如何将文字加上
            MainGame.window.blit(text,(10,10))

            #增加事件--->
            self.get_event()
            #判断我方坦克是否存活
            if MainGame.my_tank and MainGame.my_tank.live:
                #调用我方坦克显示的方法
                MainGame.my_tank.display_tank()
            else:
                MainGame.my_tank = None
            #调用敌方坦克显示的方法
            self.display_enemy_tank()

            #判断我方坦克是否存活
            if MainGame.my_tank and MainGame.my_tank.live:
                #调用坦克移动的方法---目的是让坦克连续移动
                #设置坦克移动的开关，False时，不可以移动
                if MainGame.my_tank.remove:
                    MainGame.my_tank.move()
                    #调用我方坦克与墙壁的碰撞
                    MainGame.my_tank.tank_hit_wall()
                    #调用我方坦克与敌方坦克的碰撞
                    for enemy in MainGame.enemyTank_list:
                        MainGame.my_tank.tank_collide_tank(enemy)

            #调用子弹的显示方法
            self.display_my_bullet()

            #调用敌方子弹的显示方法
            self.display_enemy_bullet()
            #调用爆炸效果的方法
            self.display_explode()
            #调用墙壁的显示方法
            self.display_wall()
            pygame.display.update() #刷新窗口

    def create_wall(self)->None:
        """
        创建墙壁
        """
        top = 200
        for i in range(6):
            # 创建墙壁-
            wall = Wall(i*145,top)
            MainGame.wall_list.append(wall)
    def display_wall(self)->None:
        """
        墙壁显示
        """
        for wall in MainGame.wall_list:
            # 判断墙壁是否存活
            if wall.live:
                wall.display_wall()
            else:
                # 从墙壁列表中删除
                MainGame.wall_list.remove(wall)
    def create_my_tank(self):
        """
        创建我方坦克
        """
        MainGame.my_tank = MyTank(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        #创建音效对象
        music = Music('img/start.wav')
        #播放音效
        music.play_music()

    def display_explode(self)->None:
        """
        显示爆炸效果
        """
        for explode in MainGame.explode_list:
            if explode.live:
                explode.display_explode()
            else:
                MainGame.explode_list.remove(explode)

    def display_my_bullet(self):
        """
        我方子弹显示
        """
        for my_bullet in MainGame.my_bullet_list:
            #判断子弹是否存活
            if my_bullet.live:
                #调用子弹显示的方法
                my_bullet.display_bullet()
                #调用子弹移动的方法
                my_bullet.move()
                #调用我方子弹与敌方坦克的碰撞检测
                my_bullet.hit_enemy_tank()
                #调用我方子弹与墙壁的碰撞检测
                my_bullet.hit_wall()
            else:
                MainGame.my_bullet_list.remove(my_bullet) # 如果子弹死亡，从列表中删除

    def create_enemy_tank(self):
        """
        创建敌方坦克
        """
        self.enemy_top = 100
        self.enemy_speed = 3
        for i in range(MainGame.enemyTank_count):
            left = random.randint(1,7) * 100 # 随机生成敌方坦克的left值
            enemy = EnemyTank(left,self.enemy_top,self.enemy_speed) # 创建敌方坦克对象
            MainGame.enemyTank_list.append(enemy) # 将敌方坦克添加到列表中

    def display_enemy_tank(self)->None:
        """
        敌方坦克显示
        """
        for enemy in MainGame.enemyTank_list:
            #判断敌方坦克是否存活
            if enemy.live:
                #调用敌方坦克显示的方法
                enemy.display_tank()
                #调用敌方坦克移动的方法
                # enemy.move()
                enemy.rand_move()
                #调用敌方坦克与墙壁的碰撞
                enemy.tank_hit_wall()
                #调用敌方坦克与我方坦克的碰撞
                if MainGame.my_tank and MainGame.my_tank.live:
                    enemy.tank_collide_tank(MainGame.my_tank)
                #调用敌方坦克射击的方法
                enemy_bullet = enemy.shot()
                #如果子弹为None，不加入到敌方子弹列表中
                if enemy_bullet:
                    # 将子弹加入到敌方子弹列表中
                    MainGame.enemy_bullet_list.append(enemy_bullet)
            else:
                #从列表中删除
                MainGame.enemyTank_list.remove(enemy)
                # MainGame.enemyTank_count -= 1

    def display_enemy_bullet(self):
        """
        敌方子弹显示
        """
        for enemy_bullet in MainGame.enemy_bullet_list:
            #判断子弹是否存活
            if enemy_bullet.live:
                #调用子弹显示的方法
                enemy_bullet.display_bullet()
                enemy_bullet.move()
                # 判断是否击中我方坦克
                enemy_bullet.hit_my_tank()
                # 判断是否击中墙壁
                enemy_bullet.hit_wall()
            else:
                MainGame.enemy_bullet_list.remove(enemy_bullet) # 如果子弹死亡，从列表中删除

    def get_text_surface(self,text):
        """
        获取文字的Surface
        :param text:
        :return:
        """
        pygame.font.init()  # 初始化字体
        # print(pygame.font.get_fonts()) # 查看所有可用字体--如果字体名字不对，会报错
        font = pygame.font.SysFont("songti", 18) # 创建字体对象
        # 绘制文字信息
        text_surface = font.render(text,True,TEXT_COLOR)
        #将绘制的文字信息返回
        return text_surface

    def get_event(self):
        """
        获取所有事件（鼠标事件，键盘事件）
        :return:
        """
        event_list = pygame.event.get() # 获取所有事件
        #遍历事件
        for event in event_list:
            #判断事件类型，如果是退出事件，则调用结束方法
            if event.type == pygame.QUIT:
                self.end_game()

            #如果是键盘按下事件
            if event.type == pygame.KEYDOWN:
                #如果我方坦克死亡，按下esc键，重生我方坦克
                if not MainGame.my_tank and event.key == pygame.K_ESCAPE:
                    self.create_my_tank()
                #判断我方坦克是否存活
                if MainGame.my_tank and MainGame.my_tank.live:
                    #判断按下的是上、下、左、右
                    if event.key == pygame.K_LEFT:
                        print("按下左键，坦克向左移动")
                        #修改方向
                        MainGame.my_tank.direction = 'L'
                        #调用坦克移动的方法
                        MainGame.my_tank.remove = True
                    elif event.key == pygame.K_RIGHT:
                        print("按下右键，坦克向右移动")
                        MainGame.my_tank.direction = 'R'
                        MainGame.my_tank.remove = True
                    elif event.key == pygame.K_UP:
                        print("按下上键，坦克向上移动")
                        MainGame.my_tank.direction = 'U'
                        MainGame.my_tank.remove = True
                    elif event.key == pygame.K_DOWN:
                        print("按下下键，坦克向下移动")
                        MainGame.my_tank.direction = 'D'
                        MainGame.my_tank.remove = True
                    elif event.key == pygame.K_SPACE: # 按下空格键，发射子弹
                        # 判断当前子弹列表中子弹的数量，不能超过5个
                        if len(MainGame.my_bullet_list) < 5:
                            print("发射子弹")
                            # 创建子弹对象
                            m_bullt = Bullet(MainGame.my_tank)
                            # 将子弹加入到子弹列表
                            MainGame.my_bullet_list.append(m_bullt)
                            #创建音效对象
                            music = Music('img/fire.wav')
                            #播放音效
                            music.play_music()



            #松开方向键，坦克停止移动，修改移动开关,但是要限制只有在移动的时候松开才有效
            if event.type == pygame.KEYUP and event.key in (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN):
                #判断我方坦克是否存活
                if MainGame.my_tank and MainGame.my_tank.live:
                    MainGame.my_tank.remove = False


    def end_game(self) -> None:
        """
        结束游戏
        :return:
        """
        print("谢谢使用，欢迎再次使用")
        exit()

if __name__ == '__main__':
    MainGame().start_game()