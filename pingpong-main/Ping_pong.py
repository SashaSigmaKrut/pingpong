from pygame import *
from random import randint
from time import time as timer



mixer.init()
mixer.music.load('backmus.mp3')
mixer.music.play()
stuk_sound = mixer.Sound('stuk.mp3')


#шрифты и надписи
font.init()
font1 = font.SysFont("Arial", 80)
font2 = font.SysFont("Arial", 36)
win_player2 = font1.render("ИГРОК 2 ТЫ ВЫИГРАЛ!", True,(200,0,0))
win_player1 = font1.render("ИГРОК 1 ТЫ ВЫЙГРАЛ!", True, (200,0,0))


#нам нужны такие картинки:
img_back = "back.jpg" # фон игры
img_ball = "balll.jpg" # герой
img_wall = "wall.png" # враг






#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < 400:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < 400:
           self.rect.y += self.speed





#Создаём окошко
win_width = 700
win_height = 500
display.set_caption("Ping_pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
speed_x = 5
speed_y = 5


#создаём спрайты
Player1 = Player(img_wall, 20, 50, 80, 100, 25)
Player2 = Player(img_wall, 600,  50, 80, 100, 25)
Ball = GameSprite(img_ball, 350, 250, 30, 30, 10)








#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку “Закрыть”
   for e in event.get():
       if e.type == QUIT:
           run = False


   if not finish:
       Ball.rect.x += speed_x
       Ball.rect.y += speed_y

       if Ball.rect.y > win_height-50 or Ball.rect.y < 0:
            speed_y *= -1
       #обновляем фон
       window.blit(background,(0,0))


       #пишем текст на экране
       #производим движения спрайтов


       Player2.update_r()
       Player1.update_l()


       #обновляем их в новом местоположении при каждой итерации цикла
       Player1.reset()
       Player2.reset()
       Ball.reset()



       if sprite.collide_rect(Ball, Player1) or sprite.collide_rect(Ball, Player2):
           speed_x *= -1.1
           stuk_sound.play()

       if Ball.rect.x > win_width:
           finish = True

       if Ball.rect.x < 0:
           finish = True

       display.update()
   #цикл срабатывает каждую 0.05 секунд
   else:
       window.blit(background,(0,0))
       
       if Ball.rect.x > win_width:
           window.blit(win_player1 ,(0,100))
           #player2 lose
       if Ball.rect.x < 0:
           window.blit(win_player2,(0,100))
           #player1 lose
       display.update()
   time.delay(50)