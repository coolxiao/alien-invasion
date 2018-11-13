import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def rum_game():
    # 初始化
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_setting, screen)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)


if __name__ == '__main__':
    rum_game()
