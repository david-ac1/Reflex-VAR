import asyncio
import reflex as rx
from enum import Enum

class GamePhase(Enum):
    IDLE = "IDLE"
    PLAYING = "PLAYING"
    VAR_FREEZE = "VAR_FREEZE"
    INPUT_WAIT = "INPUT_WAIT"
    RESULT = "RESULT"
    LEADERBOARD = "LEADERBOARD"

class ScoreEntry(rx.Model, table=True):
    initials: str
    accuracy: float
    timestamp: str

class GameState(rx.State):
    phase: GamePhase = GamePhase.IDLE
    
    # User Input
    user_initials: str = ""
    
    # GRID Data / Game Logic
    target_x: float = 0.5
    target_y: float = 0.5
    user_x: float = 0.0
    user_y: float = 0.0
    accuracy: float = 0.0
    
    # Telemetry data for display
    player_name: str = "C9_OXY"
    event_type: str = "ability_cast"
    timestamp: str = "00:14:22:04"
    frame_id: str = "RX-9922-84"

    def submit_score(self):
        if self.user_initials:
            with rx.session() as session:
                session.add(
                    ScoreEntry(
                        initials=self.user_initials.upper(),
                        accuracy=self.accuracy,
                        timestamp=self.timestamp,
                    )
                )
                session.commit()
            self.user_initials = ""
            return rx.redirect("/leaderboard") # Or update phase

    @rx.var
    def leaderboard(self) -> list[ScoreEntry]:
        with rx.session() as session:
            return session.exec(
                ScoreEntry.select().order_by(ScoreEntry.accuracy.desc()).limit(5)
            ).all()

    async def start_var_review(self):
        print("[DEBUG_LOG] start_var_review called")
        self.phase = GamePhase.PLAYING
        
        # Option A: Fetch live data from GRID
        from .grid_service import GridService
        clutch_data = GridService.fetch_live_clutch()
        
        self.player_name = clutch_data["player"]
        self.event_type = clutch_data["event"]
        self.timestamp = clutch_data["timestamp"]
        self.target_x = clutch_data["target_x"]
        self.target_y = clutch_data["target_y"]
        self.frame_id = clutch_data["frame_id"]
        
        # Simulate the "Video" playing for 2 seconds
        yield
        await asyncio.sleep(2)
        print("[DEBUG_LOG] Transitioning to VAR_FREEZE")
        self.phase = GamePhase.VAR_FREEZE

    def trigger_freeze(self):
        print("[DEBUG_LOG] trigger_freeze called")
        self.phase = GamePhase.VAR_FREEZE
    
    def handle_click(self, event_dict: dict):
        # event_dict usually contains page_x, page_y or client_x, client_y
        print(f"[DEBUG_LOG] handle_click called with: {event_dict}")
        if self.phase == GamePhase.VAR_FREEZE:
            # Extract coordinates from Reflex click event
            # Note: This depends on the exact event structure, typically clientX/clientY
            try:
                # Approximate normalization based on 1080p kiosk expectation
                # In a production kiosk, we would use screen dimensions
                raw_x = event_dict.get("clientX", 0)
                raw_y = event_dict.get("clientY", 0)
                
                self.user_x = raw_x / 1920.0
                self.user_y = raw_y / 1080.0
            except Exception as e:
                print(f"[DEBUG_LOG] Error parsing click coords: {e}")
                self.user_x = 0.5
                self.user_y = 0.5
            
            # Use GridService to calculate accuracy
            from .grid_service import GridService
            self.accuracy = round(GridService.calculate_pro_accuracy(
                (self.user_x, self.user_y), 
                (self.target_x, self.target_y)
            ), 1)
            self.phase = GamePhase.RESULT

    def reset_game(self):
        self.phase = GamePhase.IDLE
        self.accuracy = 0.0
        self.user_x = 0.0
        self.user_y = 0.0
