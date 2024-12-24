'''
需求分析：
    1. 坦克类
        1.1 我方坦克
        1.2 敌方坦克
        坦克显示
        坦克移动
        坦克射击
    2. 子弹类
        子弹显示
        子弹移动
    3.墙壁类
        墙壁显示
    4.爆炸效果类
        爆炸效果显示
    5.音效类
        播放音效
    6.游戏主窗口类
        开始游戏
        结束游戏
'''

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
    def __init__(self) -> None:
        pass
    def start_game(self) -> None:
        """
        开始游戏
        """
        pass
    def end_game(self) -> None:
        """
        结束游戏
        """
        pass