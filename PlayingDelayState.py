import ZedLib
import pygame

class PlayingDelayState(ZedLib.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.delay_timer = ZedLib.Timer(1500)

    def Update(self):
        self.delay_timer.Update(self.delta)
        if self.delay_timer.complete:
            self.game.ChangeState(self.game.playing_state)

    def HandleKeyDownEvent(self, key):
        if key == pygame.K_ESCAPE:
            self.game.Pause()

    def DrawScreen(self):
        self.game.playing_state.DrawScreen()
