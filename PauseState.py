import pygame
import ZedLib


class PauseState(ZedLib.GameState):
    def __init__(self, game):
        super().__init__(game)

        # Paused splash
        paused_splash = ZedLib.Surface(ZedLib.\
                LoadImage("Resources/Splashes/Paused.png", scale=6))
        paused_splash.PlaceInCenter(self.game.screen, y_offset=-100)

        self.AddSurfaces(paused_splash)

        # Resume button
        resume_b_spritesheet = ZedLib.ButtonSpritesheet(\
                "Resources/Buttons/Resume.png", scale=4)
        resume_button = ZedLib.Button(resume_b_spritesheet.GetVerticalStrip(0),
                                    self.ReturnToPlaying)
        resume_button.PlaceInCenterX(self.game.screen, -400)
        resume_button.rect.bottom = self.game.screen_height - 50

        # Options button
        options_b_spritesheet = ZedLib.ButtonSpritesheet(
                "Resources/Buttons/Options.png", scale=4)
        options_button = ZedLib.Button(options_b_spritesheet.GetVerticalStrip(0),
                                       self.GoToOptions)
        options_button.PlaceInCenterX(self.game.screen)
        options_button.rect.bottom = self.game.screen_height - 50

        # Exit button
        exit_b_spritesheet = ZedLib.ButtonSpritesheet(\
                "Resources/Buttons/Exit.png", scale=4)
        exit_button = ZedLib.Button(exit_b_spritesheet.GetVerticalStrip(0),
                                    self.game.ReturnToMainMenu)
        exit_button.PlaceInCenterX(self.game.screen, 400)
        exit_button.rect.bottom = self.game.screen_height - 50

        self.AddButtons(resume_button, options_button, exit_button)

    def HandleKeyDownEvent(self, key):
        if key == pygame.K_ESCAPE:
            self.game.ReturnToPlayingState()

    def ReturnToPlaying(self):
        self.game.ResetPlayingDelayState()
        self.game.ChangeState(self.game.playing_delay_state)

    def GoToOptions(self):
        self.game.options_state.state_to_return_to = self.game.pause_state
        self.game.ChangeState(self.game.options_state)
