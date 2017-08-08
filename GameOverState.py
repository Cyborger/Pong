import ZedLib


class GameOverState(ZedLib.GameState):
    def __init__(self, game):
        super().__init__(game)
        gameover_splash = ZedLib.Surface(ZedLib.LoadImage("Resources/Splashes/GameOver.png", scale=4))
        gameover_splash.PlaceInCenterX(self.game.screen)
        gameover_splash.PlaceInCenterY(self.game.screen, offset=-100)
        self.AddSurfaces(gameover_splash)
        self.delay_timer = ZedLib.Timer(2000)

    def Update(self):
        self.delay_timer.Update(self.delta)
        if self.delay_timer.complete:
            self.game.ChangeState(self.game.main_menu_state)

    def DrawScreen(self):
        self.DrawSurfaces()
