import sys
import pygame

#相应按键
def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
                #飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
# 响应松开
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False




def check_events(ship):
    #相应鼠标和键盘事件
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            


                
    #更新屏幕上的图像，并切换到新的图像
def update_screen(ai_settings,screen,ship):
    #绘制屏幕背景
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘制的图像可见
    pygame.display.flip()