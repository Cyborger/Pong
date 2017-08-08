import ZedLib


class MainMenuState(ZedLib.GameState):
    def __init__(self, game):
        super().__init__(game)
        # PONG splash
        pong_splash = ZedLib.Surface(ZedLib.LoadImage("Resources/Splashes/Pong.png", 6))
        pong_splash.PlaceInCenter(self.game.screen, y_offset=-100)
        self.AddSurfaces(pong_splash)
        # Start button
        start_b_spritesheet = ZedLib.ButtonSpritesheet(\
                "Resources/Buttons/Start.png", scale=4)
        start_button = ZedLib.Button(start_b_spritesheet.GetVerticalStrip(0),
                                     self.EnterGame)
        start_button.PlaceInCenterX(self.game.screen, -400)
        start_button.rect.bottom = self.game.screen_height - 50

        # Options button
        options_b_spritesheet = ZedLib.ButtonSpritesheet(\
                "Resources/Buttons/Options.png", scale=4)
        options_button = ZedLib.Button(options_b_spritesheet.GetVerticalStrip(0),
                                       self.GoToOptions)
        options_button.PlaceInCenterX(self.game.screen)
        options_button.rect.bottom = self.game.screen_height - 50

        # Exit button
        exit_b_spritesheet = ZedLib.ButtonSpritesheet(\
                "Resources/Buttons/Exit.png", scale=4)
        exit_button = ZedLib.Button(exit_b_spritesheet.GetVerticalStrip(0),
                                    self.ExitGame)
        exit_button.PlaceInCenterX(self.game.screen, 400)
        exit_button.rect.bottom = self.game.screen_height - 50

        self.AddButtons(start_button, options_button, exit_button)

    def Update(self):
        self.UpdateButtons()

    def DrawScreen(self):
        self.DrawButtons()
        self.DrawSurfaces()

    def EnterGame(self):
        self.game.ResetPlayingState()
        self.game.ResetPlayingDelayState()
        self.game.ChangeState(self.game.playing_delay_state)

    def GoToOptions(self):
        self.game.ChangeState(self.game.options_state)
        self.game.options_state.state_to_return_to = self.game.main_menu_state

    def ExitGame(self):
        self.game.running = False
