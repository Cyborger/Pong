import pygame
import ZedLib

class Paddle(ZedLib.GameSprite):
    def __init__(self):
        super().__init__(ZedLib.LoadImage("Resources/Paddles/MediumPaddle.png", scale=2))
        self.speed = 5.0
        self.up_key = pygame.K_w
        self.down_key = pygame.K_s
        self.ai_controlled = False

    def HandleInput(self):
        key_presses = pygame.key.get_pressed()
        if key_presses[self.up_key]:
            self.move_y -= self.speed
        if key_presses[self.down_key]:
            self.move_y += self.speed

    def AIControl(self, ball):
        print("Doin some fancy ai stuff")

    def SetControlScheme(self, up_key, down_key):
        self.up_key = up_key
        self.down_key = down_key
