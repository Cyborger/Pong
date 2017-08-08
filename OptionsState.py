import ZedLib

class OptionsState(ZedLib.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.state_to_return_to = None

        fullscreen_b_spritesheet = ZedLib.ButtonSpritesheet(\
                "Resources/Buttons/Fullscreen.png", scale=4)
        fullscreen_button = ZedLib.Button(fullscreen_b_spritesheet.GetVerticalStrip(0),
                                          self.game.render_screen.SetFullscreenWindow)
        fullscreen_button.PlaceInCenterY(self.game.screen)
        fullscreen_button.PlaceInCenterX(self.game.screen, offset=-275)

        windowed_b_spritesheet = ZedLib.ButtonSpritesheet(\
                "Resources/Buttons/Windowed.png", scale=4)
        windowed_button = ZedLib.Button(windowed_b_spritesheet.GetVerticalStrip(0),
                                        self.game.render_screen.SetResizableWindow)
        windowed_button.PlaceInCenterX(self.game.screen, offset=275)
        windowed_button.PlaceInCenterY(self.game.screen)

        back_b_spritesheet = ZedLib.ButtonSpritesheet(\
                "Resources/Buttons/Back.png", scale=4)
        back_button = ZedLib.Button(back_b_spritesheet.GetVerticalStrip(0),
                                    self.ReturnToLastState)
        back_button.rect.x = 50
        back_button.rect.bottom = self.game.screen_height - 50
        self.AddButtons(fullscreen_button, windowed_button, back_button)

    def ReturnToLastState(self):
        self.game.ChangeState(self.state_to_return_to)

    def Update(self):
        self.UpdateButtons()

    def DrawScreen(self):
        self.DrawButtons()
