import pygame

# Initialize the game engine
pygame.init()
#创建一个窗口
pygame.display.set_mode((800, 600))

#设置窗口标题
pygame.display.set_caption('坦克大战1.0')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #刷新窗口
    pygame.display.update()