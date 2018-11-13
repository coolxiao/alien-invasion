import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def rum_game():
    # 初始化
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_setting, screen, ship, aliens)
    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(ai_setting, aliens)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets)


if __name__ == '__main__':
    rum_game()
