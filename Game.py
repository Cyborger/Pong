import ZedLib
from MainMenuState import MainMenuState
from PlayingState import PlayingState
from PauseState import PauseState
from PlayingDelayState import PlayingDelayState
from OptionsState import OptionsState
from GameOverState import GameOverState

class Game(ZedLib.Game):
    def __init__(self):
        super().__init__(1280, 720)

        self.main_menu_state = MainMenuState(self)
        self.playing_delay_state = PlayingDelayState(self)
        self.playing_state = PlayingState(self)
        self.pause_state = PauseState(self)
        self.options_state = OptionsState(self)
        self.game_over_state = GameOverState(self)
        self.ChangeState(self.main_menu_state)

    def EnterGame(self):
        self.ResetPlayingState()
        self.ResetPlayingDelayState()
        self.ChangeState(self.playing_delay_state)

    def ResetPlayingState(self):
        self.playing_state = PlayingState(self)

    def ResetPlayingDelayState(self):
        self.playing_delay_state = PlayingDelayState(self)

    def ReturnToMainMenu(self):
        self.ChangeState(self.main_menu_state)
