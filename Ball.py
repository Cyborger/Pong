import pygame
import ZedLib

class Ball(ZedLib.Projectile):
    def __init__(self, angle, x=0.0, y=0.0):
        self.speed = 8.0
        super().__init__(ZedLib.LoadImage("Resources/Balls/5Radius.png"), angle, self.speed, x, y)

    def VerticalCollisionOccured(self, _):
        self.InvertVertically()

    def HorizontalCollisionOccured(self, _):
        self.InvertHorizontally()
