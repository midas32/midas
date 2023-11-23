import pygame
import time
pygame.init()
back = (200, 255, 255)
clock = pygame.time.Clock()
pygame.display.set_caption('game')
run = True
window = pygame.display.set_mode((700, 500))
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, x, y, weight, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture), (weight, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def reset(self):
        self.rect.x = self.x
        self.rect.y = self.y
class Player(GameSprite):
    def __init__(self, picture, x, y, weight, height, x_speed, y_speed):
        super().__init__(picture, x, y, weight, height)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.bullets = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x > 650:
            self.rect.x = 650
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > 430:
            self.rect.y = 430
        if self.rect.y < 0:
            self.rect .y = 0
    def fire(self):
        bullet = Bullet('bullet.jpg', self.rect.right, self.rect.centery, 20, 30, 5)
        self.bullets.add(bullet)

        

class Enemy(GameSprite):
    def __init__(self, picture, x1, y1, weight, height, x1_speed, y1_speed):
        super().__init__(picture, x1, y1, weight, height)
        self.x1_speed = x1_speed
        self.y1_speed = y1_speed
    def update(self):
        self.rect.x += self.x1_speed
        self.rect.y += self.y1_speed
        if self.rect.y < 100:
            self.y1_speed *= -1
        elif self.rect.y > 300:
            self.y1_speed *= -1
class Bullet(GameSprite):
    def __init__(self, picture, x1, y1, weight, height, x2_speed):
        super().__init__(picture, x1, y1, weight, height)
        self.x_speed = x2_speed
    def update(self):
        self.rect.x += self.x_speed
        if self.rect.x > 650:
            self.kill

    

player = Player('player.png', 200, 100, 50, 70, 0, 0)
wall_1 = GameSprite('mainwall.png', 0, 0, 700, 500)
photo = GameSprite('mainwall.png',100, 200, 80, 90)
miniwall = GameSprite('platform2_v.png', 300, 300, 200, 50)
miniwall1 = GameSprite('platform2_v.png', 300, 130, 50, 230)
miniwall2 = GameSprite('platform2_v.png', 300, 130, 200, 50)
win = GameSprite('win.jpg', 0, 0, 700, 500)
wait = 5
enemy = Enemy('enemyy.png', 500, 300, 50, 70, 0, 5)
finish = GameSprite('finish.png', 600, 400, 100,100)
loose = GameSprite('loose.jpg', 0, 0, 700, 500)
enemy2 = Enemy('enemyy.png', 300, 150, 70, 100, 0, 5)
barriers = pygame.sprite.Group()
barriers.add(miniwall)
barriers.add(miniwall1)
barriers.add(miniwall2)
enemies = pygame.sprite.Group()
enemies.add(enemy)

final = False
while run:
    if final:
        wait -= 1
        print(wait)
        time.sleep(1)
        if wait == 0:
            final = False
            wait = 5
        continue
    platforms_touched = pygame.sprite.spritecollide(player, barriers, False)
    if platforms_touched:
        player.reset()
    clock.tick(40)
    pygame.display.update()
    photo.draw()
    wall_1.draw()
    player.draw()
    player.update()
    miniwall.draw()
    miniwall1.draw()
    miniwall2.draw()
    enemies.draw(window)
    finish.draw()
    enemies.update()
    player.bullets.draw(window)
    player.bullets.update()
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                player.y_speed = -5
            elif e.key == pygame.K_a:
                player.x_speed = -7
            elif e.key == pygame.K_s:
                player.y_speed = 5
            elif e.key == pygame.K_d:
                player.x_speed = 7
            elif e.key == pygame.K_SPACE:
                player.fire()
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                player.y_speed = 0
            elif e.key == pygame.K_a:
                player.x_speed = 0
            elif e.key == pygame.K_s:
                player.y_speed = 0
            elif e.key == pygame.K_d:
                player.x_speed = 0

            
        if e.type == pygame.QUIT:
            run = False
    pygame.sprite.groupcollide(player.bullets, barriers, True, False)
    pygame.sprite.groupcollide(player.bullets, enemies, True, True)
    if final != True:
        if pygame.sprite.collide_rect(player, finish):
            win.draw()
            player.update()
            player.reset()
            final = True
            pygame.display.update()
        if pygame.sprite.spritecollide(player, enemies, False):
            loose.draw()
            player.update()
            player.reset()
            final = True
            pygame.display.update()
            
