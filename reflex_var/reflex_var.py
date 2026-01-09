"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .state import GameState, GamePhase

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "REFLEX-VAR", 
                size="9",
                color="#00AEEF", # Cloud9 Blue
                font_family="Chakra Petch, sans-serif", # Cyberpunk vibe
            ),
            rx.text(
                f"Current Phase: {GameState.phase}",
                color="#7B61FF", # JetBrains Purple
                font_weight="bold",
            ),
            rx.button(
                "START VAR REVIEW",
                on_click=GameState.start_var_review,
                bg="#00AEEF",
                color="white",
                _hover={"bg": "#7B61FF"},
                padding="32px", # 4 * 8pt
                border_radius="0px", # Cyberpunk blocky style
                font_weight="bold",
            ),
            spacing="8", # 8 * 8pt = 64px or just using reflex spacing units if they map to 8pt
            align="center",
            padding="40px",
        ),
        height="100vh",
        background_color="black",
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;700&display=swap",
    ],
)
app.add_page(index)
