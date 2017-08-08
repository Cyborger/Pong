import pygame
import ZedLib
from Paddle import Paddle
from Ball import Ball

class PlayingState(ZedLib.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.paddle_1 = Paddle()
        self.paddle_2 = Paddle()
        self.paddle_2.SetControlScheme(pygame.K_UP, pygame.K_DOWN)
        self.paddle_2.rect.right = self.game.screen_width
        self.paddle_2.pos.UpdatePositionX()
        self.paddles = [self.paddle_1, self.paddle_2]

        self.ball = Ball(30, self.game.screen_width / 2, 0)

        self.top_border = ZedLib.CollisionObject(self.game.screen_width, 10,
                                                 0, -10)
        self.bottom_border = ZedLib.CollisionObject(self.game.screen_width, 10,
                                                    0, self.game.screen_height)
        self.borders = [self.top_border, self.bottom_border]

    def Update(self):
        for paddle in self.paddles:
            if paddle.ai_controlled:
                paddle.AIControl(None)
            else:
                paddle.HandleInput()
            paddle.UpdateMovement(self.borders + [self.ball])
        self.ball.UpdateMovement(self.borders + self.paddles)
        self.CheckBallOffScreen()

    def DrawSprites(self):
        for paddle in self.paddles:
            self.game.screen.blit(paddle.image, paddle.rect)
        self.game.screen.blit(self.ball.image, self.ball.rect)

    def HandleKeyDownEvent(self, key):
        if key == pygame.K_ESCAPE:
            self.Pause()

    def CheckBallOffScreen(self):
        if ((self.ball.rect.right > self.game.screen_width) or
                (self.ball.rect.left < 0)):
            self.GameOver()

    def Pause(self):
        self.game.ChangeState(self.game.pause_state)

    def GameOver(self):
        self.game.ChangeState(self.game.game_over_state)
