from helpers import *
import random

class Enemy : 
    def __init__(self) :
        chooseDir = random.randint(1, 4) # 1 ~ 4까지 랜덤하게 선택
        if (chooseDir == S or chooseDir == N) : # Case S, N
            self.px = random.randint(0, WIDTH)
            self.x_speed = random.uniform(-1, 1)
            if (chooseDir == S) : # 남쪽
                self.py = HEIGHT
                self.y_speed = random.uniform(-1, 0)
            else : # 북쪽
                self.py = 0
                self.y_speed = random.uniform(0, 1)
        else : # Case W, E
            self.py = random.randint(0, HEIGHT)
            self.y_speed = random.uniform(-1, 1)
            if (chooseDir == E) : # 동쪽
                self.px = WIDTH
                self.x_speed = random.uniform(-1, 0)
            else : # 서쪽
                self.px = 0
                self.x_speed = random.uniform(0, 1)
