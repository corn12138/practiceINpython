'''
    移动坦克的功能优化
'''
import pygame
from time import sleep
#设置通用属性
BG_COLOR = pygame.Color(0,0,0) # 设置窗口背景颜色
SCREEN_WIDTH = 800  # 设置窗口的宽度
SCREEN_HEIGHT = 600 # 设置窗口的高度
TEXT_COLOR = pygame.Color(255,0,0) # 设置文字颜色

class Tank:
    """
    坦克类
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
    def __init__(self) -> None:
        pass

class EnemyTank(Tank):
    """
    敌方坦克
    """
    def __init__(self) -> None:
        pass

class Bullet:
    """
    子弹类
    """
    def __init__(self) -> None:
        pass
    def display_bullet(self) -> None:
        """
        子弹显示
        """
        pass
    def move(self) -> None:
        """
        子弹移动
        """
        pass

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
        MainGame.my_tank = Tank(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)

        #使窗口保持显示状态-刷新窗口
        while True:
            sleep(0.02) #每次休眠0.02s
            #给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            #增加提示文字
            # 1.变量增加文字内容
            num = 6
            text = self.get_text_surface('敌方坦克剩余数量{0}'.format(num))
            # 2.如何将文字加上
            MainGame.window.blit(text,(10,10))

            #增加事件--->
            self.get_event()
            #调用坦克显示的方法
            MainGame.my_tank.display_tank()
            #调用坦克移动的方法---目的是让坦克连续移动
            #设置坦克移动的开关，False时，不可以移动
            if MainGame.my_tank.remove:
                MainGame.my_tank.move()

            pygame.display.update()


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