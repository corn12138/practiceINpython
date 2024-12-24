'''
增加了文字的操作与展示
'''
import pygame
#设置通用属性
BG_COLOR = pygame.Color(0,0,0) # 设置窗口背景颜色
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TEXT_COLOR = pygame.Color(255,0,0) # 设置文字颜色

class Tank:
    """
    坦克类
    """
    def __init__(self) -> None:
        pass

    def display_tank(self) -> None:
        """
        坦克显示
        """
        pass
    def move(self) -> None:
        """
        坦克移动
        """
        pass
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
        pygame.display.set_caption("坦克大战")
        #使窗口保持显示状态-刷新窗口
        while True:
            #给窗口设置填充色
            MainGame.window.fill(BG_COLOR)
            #增加提示文字
            # 1.变量增加文字内容
            num =6
            text = self.get_text_surface('敌方坦克剩余数量{0}'.format(num))
            # 2.如何将文字加上
            MainGame.window.blit(text,(10,10))

            #调用事件处理的方法-目的是将事件交给对应的对象处理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
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



    def end_game(self) -> None:
        """
        结束游戏
        :return:
        """
        print("谢谢使用，欢迎再次使用")
        exit()

if __name__ == '__main__':
    MainGame().start_game()