import reflex as rx
from enum import Enum

class GamePhase(Enum):
    IDLE = "IDLE"
    PLAYING = "PLAYING"
    VAR_FREEZE = "VAR_FREEZE"
    INPUT_WAIT = "INPUT_WAIT"
    RESULT = "RESULT"

class GameState(rx.State):
    phase: GamePhase = GamePhase.IDLE
    
    def start_var_review(self):
        self.phase = GamePhase.VAR_FREEZE
