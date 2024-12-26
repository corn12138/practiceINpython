'''
    我方坦克发射的子弹移动
'''
import pygame
from time import sleep
import random
#设置通用属性
BG_COLOR = pygame.Color(0,0,0) # 设置窗口背景颜色
SCREEN_WIDTH = 800  # 设置窗口的宽度
SCREEN_HEIGHT = 600 # 设置窗口的高度
TEXT_COLOR = pygame.Color(255,0,0) # 设置文字颜色

class Tank:
    """
    坦克类
    """
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

class MyTank(Tank):
    """
    我方坦克
    """
    def __init__(self,left,top) -> None:
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
            # else:
            #     #移除子弹
            #     MainGame.my_bullet_list.remove(self)
        elif self.driction == 'R':
            if self.rect.left+self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
            # else:
            #     MainGame.my_bullet_list.remove(self)
        elif self.driction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            # else:
            #     MainGame.my_bullet_list.remove(self)
        elif self.driction == 'D':
            if self.rect.top+self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
            # else:
            #     MainGame.my_bullet_list.remove(self)

class Wall:
    """
    墙壁类
    """
    def __init__(self) -> None:
        pass
    def display_wall(self) -> None:
        """
        墙壁显示
        """
        pass

class Explode:
    """
    爆炸效果类
    """
    def __init__(self) -> None:
        pass
    def display_explode(self) -> None:
        """
        爆炸效果显示
        """
        pass

class Music:
    """
    音效类
    """
    def __init__(self) -> None:
        pass
    def play_music(self) -> None:
        """
        播放音效
        """
        pass

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
        MainGame.my_tank = MyTank(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        #创建敌方坦克
        self.create_enemy_tank()

        #使窗口保持显示状态-刷新窗口
        while True:
            sleep(0.02) #每次休眠0.02s
            #给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            #增加提示文字
            # 1.变量增加文字内容
            # num = 6
            text = self.get_text_surface('敌方坦克剩余数量{0}'.format(MainGame.enemyTank_count))
            # 2.如何将文字加上
            MainGame.window.blit(text,(10,10))

            #增加事件--->
            self.get_event()
            #调用我方坦克显示的方法
            MainGame.my_tank.display_tank()
            #调用敌方坦克显示的方法
            self.display_enemy_tank()

            #调用坦克移动的方法---目的是让坦克连续移动
            #设置坦克移动的开关，False时，不可以移动
            if MainGame.my_tank.remove:
                MainGame.my_tank.move()

            #调用子弹的显示方法
            self.display_my_bullet()

            pygame.display.update() #刷新窗口
    def display_my_bullet(self):
        """
        我方子弹显示
        """
        for my_bullet in MainGame.my_bullet_list:
            #调用子弹显示的方法
            my_bullet.display_bullet()
            #调用子弹移动的方法
            my_bullet.move()
    def create_enemy_tank(self):
        """
        创建敌方坦克
        """
        self.enemy_top = 100
        self.enemy_speed = 5
        for i in range(MainGame.enemyTank_count):
            left = random.randint(1,7) * 100 # 随机生成敌方坦克的left值
            enemy = EnemyTank(left,self.enemy_top,self.enemy_speed) # 创建敌方坦克对象
            MainGame.enemyTank_list.append(enemy) # 将敌方坦克添加到列表中

    def display_enemy_tank(self)->None:
        """
        敌方坦克显示
        """
        for enemy in MainGame.enemyTank_list:
            #调用敌方坦克显示的方法
            enemy.display_tank()
            #调用敌方坦克移动的方法
            # enemy.move()
            enemy.rand_move()
    #
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
                    print("发射子弹")
                    # 创建子弹对象
                    m_bullt = Bullet(MainGame.my_tank)
                    # 将子弹加入到子弹列表
                    MainGame.my_bullet_list.append(m_bullt)


            #松开方向键，坦克停止移动，修改移动开关,但是要限制只有在移动的时候松开才有效
            if event.type == pygame.KEYUP and event.key in (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN):
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