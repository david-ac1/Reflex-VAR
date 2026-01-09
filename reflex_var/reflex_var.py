"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .state import GameState, GamePhase

# Constants for colors based on guidelines
COLOR_BACKGROUND = "#0B0E11"
COLOR_SURFACE = "#161B22"
COLOR_PRIMARY = "#00AEEF"
COLOR_SECONDARY = "#7B61FF"
COLOR_SUCCESS = "#00FF94"
COLOR_CRITICAL = "#FF4D00"

def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.icon(tag="activity", color=COLOR_PRIMARY, size=24),
                rx.heading(
                    "REFLEX VAR",
                    size="5",
                    color="white",
                    font_family="JetBrains Mono",
                    font_weight="bold",
                    letter_spacing="0.2em",
                ),
                rx.text("// SYSTEM ACTIVE", color=COLOR_PRIMARY, font_family="JetBrains Mono", size="1"),
                align="center",
                spacing="4",
            ),
            rx.spacer(),
            rx.hstack(
                rx.text("ID: KSK-09-C9", color="white", opacity=0.6, font_family="JetBrains Mono", size="1"),
                rx.box(width="1px", height="20px", background_color="white", opacity=0.2),
                rx.text("V1.0.4-BETA", color="white", opacity=0.6, font_family="JetBrains Mono", size="1"),
                align="center",
                spacing="4",
            ),
            width="100%",
            padding="20px 40px",
            background_color=f"{COLOR_BACKGROUND}CC",
            backdrop_filter="blur(12px)",
            border_bottom=f"1px solid {COLOR_SURFACE}",
            position="fixed",
            top="0",
            z_index="50",
        ),
        width="100%",
    )

def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.text("FRAME_ID:", color=COLOR_PRIMARY, font_family="JetBrains Mono", size="1", font_weight="bold"),
                rx.text(GameState.frame_id, color="white", opacity=0.6, font_family="JetBrains Mono", size="1"),
                spacing="2",
            ),
            rx.hstack(
                rx.text("SMPTE:", color=COLOR_PRIMARY, font_family="JetBrains Mono", size="1", font_weight="bold"),
                rx.text(GameState.timestamp, color="white", font_family="JetBrains Mono", size="1"),
                spacing="2",
            ),
            rx.spacer(),
            rx.hstack(
                rx.text("AI_VERSION:", color=COLOR_SECONDARY, font_family="JetBrains Mono", size="1", font_weight="bold"),
                rx.text("v4.2.0-STABLE", color="white", opacity=0.6, font_family="JetBrains Mono", size="1"),
                spacing="2",
            ),
            width="100%",
            padding="10px 40px",
            background_color=COLOR_BACKGROUND,
            border_top=f"1px solid {COLOR_SURFACE}",
            position="fixed",
            bottom="0",
            z_index="50",
        ),
        width="100%",
    )

def idle_view() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "ELITE PERFORMANCE ANALYSIS SYSTEM",
                color="white",
                opacity=0.6,
                size="2",
                font_family="JetBrains Mono",
                letter_spacing="0.4em",
                margin_bottom="40px",
            ),
            rx.box(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="play", size=24),
                        rx.text("START VAR REVIEW"),
                        align="center",
                    ),
                    on_click=GameState.start_var_review,
                    background_color=COLOR_PRIMARY,
                    color=COLOR_BACKGROUND,
                    padding="32px 64px",
                    font_size="24px",
                    font_family="JetBrains Mono",
                    font_weight="black",
                    border_radius="12px",
                    position="relative",
                    z_index="10",
                    _hover={"transform": "scale(1.05)", "background_color": "#33C0FF"},
                    transition="all 0.2s ease-in-out",
                ),
                position="relative",
                _before={
                    "content": "''",
                    "position": "absolute",
                    "inset": "-4px",
                    "background_color": COLOR_PRIMARY,
                    "opacity": "0.4",
                    "filter": "blur(20px)",
                    "border_radius": "12px",
                    "z_index": "0",
                },
            ),
            rx.text(
                "TOUCH SCREEN OR PRESS ANY KEY TO BEGIN",
                color=COLOR_PRIMARY,
                size="1",
                font_family="JetBrains Mono",
                font_weight="bold",
                letter_spacing="0.2em",
                margin_top="40px",
                animation="pulse 2s infinite",
            ),
            align="center",
            spacing="4",
        ),
        on_click=GameState.start_var_review,
        height="100vh",
        width="100vw",
        background="radial-gradient(circle, #161B22 0%, #0B0E11 100%)",
        cursor="pointer",
    )

def playing_view() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("REPLAYING ACTION...", color=COLOR_PRIMARY, font_family="JetBrains Mono"),
            rx.video(
                url=GameState.video_url,
                playing=True,
                muted=True,
                controls=False,
                width="800px",
                height="450px",
                border_radius="12px",
            ),
            spacing="4",
        ),
        height="100vh",
        background_color=COLOR_BACKGROUND,
    )

def var_freeze_view() -> rx.Component:
    return rx.box(
        header(),
        rx.center(
            rx.box(
                # The "Video" Frame (frozen at the end of the replay)
                rx.box(
                    rx.video(
                        url=GameState.video_url,
                        playing=False,
                        muted=True,
                        controls=False,
                        width="100%",
                        height="100%",
                    ),
                    width="92vw",
                    height="78vh",
                    border_radius="12px",
                    border=f"4px solid {COLOR_SECONDARY}",
                    box_shadow=f"0 0 20px {COLOR_SECONDARY}66",
                    overflow="hidden",
                    position="relative",
                    filter="grayscale(50%) brightness(70%)",
                    on_click=GameState.handle_click,
                ),
                # Dynamic Scan Line
                rx.box(
                    width="100%",
                    height="2px",
                    background=f"linear-gradient(to right, transparent, {COLOR_SECONDARY}, transparent)",
                    position="absolute",
                    top="0",
                    left="0",
                    z_index="5",
                    # Inline keyframes for better compatibility
                    style={
                        "@keyframes scan": {
                            "0%": {"top": "0%"},
                            "100%": {"top": "100%"},
                        },
                        "animation": "scan 3s linear infinite",
                    },
                    pointer_events="none",
                ),
                # Glassmorphism Scanning Overlay
                rx.box(
                    rx.text(
                        "SCANNING PLAY... SELECT TARGET",
                        color="white",
                        font_family="JetBrains Mono",
                        font_size="24px",
                        font_weight="bold",
                        letter_spacing="0.4em",
                        animation="pulse 1.5s infinite",
                    ),
                    position="absolute",
                    top="50%",
                    left="50%",
                    transform="translate(-50%, -50%)",
                    padding="24px 40px",
                    background_color="rgba(22, 27, 34, 0.6)",
                    backdrop_filter="blur(12px)",
                    border=f"1px solid {COLOR_SECONDARY}80",
                    border_radius="12px",
                    pointer_events="none",
                ),
                # UI Elements for Progress
                rx.box(
                    rx.hstack(
                        rx.text("AI SCANNING PROGRESS", color=COLOR_SECONDARY, font_size="10px", font_weight="bold", letter_spacing="0.1em"),
                        rx.spacer(),
                        rx.text("88%", color=COLOR_SECONDARY, font_family="JetBrains Mono", font_size="10px"),
                        width="100%",
                        margin_bottom="8px",
                    ),
                    rx.box(
                        rx.box(
                            width="88%",
                            height="100%",
                            background_color=COLOR_SECONDARY,
                            border_radius="full",
                        ),
                        width="100%",
                        height="6px",
                        background_color="rgba(255, 255, 255, 0.1)",
                        border_radius="full",
                    ),
                    rx.text("CALCULATING PLAYER TRAJECTORIES...", color="white", opacity=0.5, font_size="10px", font_family="JetBrains Mono", font_style="italic", margin_top="8px"),
                    position="absolute",
                    bottom="10%",
                    left="50%",
                    transform="translateX(-50%)",
                    width="384px",
                    background_color="rgba(22, 27, 34, 0.6)",
                    backdrop_filter="blur(12px)",
                    padding="16px",
                    border_radius="12px",
                    border="1px solid rgba(255, 255, 255, 0.1)",
                ),
                position="relative",
            )
        ),
        footer(),
        height="100vh",
        width="100vw",
        background_color=COLOR_BACKGROUND,
        padding_top="80px",
    )

def result_view() -> rx.Component:
    return rx.box(
        header(),
        rx.hstack(
            # Left: Analysis Result
            rx.vstack(
                rx.vstack(
                    rx.text("STATUS: ANALYSIS COMPLETE", color=COLOR_SUCCESS, size="1", font_weight="bold", letter_spacing="0.3em"),
                    rx.heading(
                        "ACCURACY - ",
                        rx.text.span(f"{GameState.accuracy}%", color=COLOR_PRIMARY),
                        size="9",
                        font_weight="black",
                        color="white",
                    ),
                    rx.cond(
                        GameState.is_live,
                        rx.badge("LIVE GRID TELEMETRY", color_scheme="green", variant="solid", margin_top="8px"),
                        rx.badge("LOCAL DATA FALLBACK", color_scheme="gray", variant="outline", margin_top="8px"),
                    ),
                    align_items="start",
                    spacing="1",
                ),
                # AI Feedback Panel
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon(tag="bot", size=32, color="white"),
                            background_color=COLOR_SECONDARY,
                            padding="16px",
                            border_radius="16px",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.text("Junie AI Feedback", color="white", font_weight="bold", font_size="18px"),
                                rx.badge("ANALYSIS PRO", background_color=f"{COLOR_SECONDARY}4D", color="white"),
                                align="center",
                            ),
                            rx.text(
                                rx.cond(
                                    GameState.accuracy > 90,
                                    "World-Class performance! Your spatial awareness matches the pro data point exactly. You correctly identified the ability cast node.",
                                    "Good attempt. You were slightly off the target coordinate. Focus on the player's pivot point for higher precision next time."
                                ),
                                color="white",
                                opacity=0.7,
                                font_size="14px",
                                max_width="600px",
                            ),
                            align_items="start",
                        ),
                        spacing="5",
                    ),
                    background_color=f"{COLOR_SECONDARY}1A",
                    border=f"1px solid {COLOR_SECONDARY}4D",
                    padding="24px",
                    border_radius="12px",
                    margin_top="24px",
                    width="100%",
                ),
                # Initials Input for Leaderboard
                rx.vstack(
                    rx.text("ENTER INITIALS TO SAVE SCORE", color="white", size="1", font_weight="bold", opacity=0.6),
                    rx.input(
                        placeholder="C9J",
                        value=GameState.user_initials,
                        on_change=GameState.set_user_initials,
                        max_length=3,
                        text_align="center",
                        font_family="JetBrains Mono",
                        font_weight="bold",
                        font_size="24px",
                        background_color=COLOR_SURFACE,
                        border=f"1px solid {COLOR_SURFACE}",
                        color=COLOR_PRIMARY,
                        width="120px",
                    ),
                    align_items="start",
                    margin_top="24px",
                    spacing="2",
                ),
                rx.button(
                    "SUBMIT SCORE",
                    on_click=GameState.submit_score,
                    background_color=COLOR_SUCCESS,
                    color=COLOR_BACKGROUND,
                    width="100%",
                    margin_top="12px",
                    font_weight="bold",
                ),
                # Option D: QR Code Share
                rx.vstack(
                    rx.text("SCAN TO TAKE SCORE HOME", color="white", size="1", font_weight="bold", opacity=0.6),
                    rx.box(
                        rx.image(
                            src=f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://reflex-var.com/share?score={GameState.accuracy}%26initials={GameState.user_initials}",
                            width="120px",
                            height="120px",
                        ),
                        padding="8px",
                        background_color="white",
                        border_radius="8px",
                    ),
                    align_items="center",
                    width="100%",
                    margin_top="24px",
                    spacing="2",
                ),
                rx.button(
                    "RETRY CHALLENGE",
                    on_click=GameState.reset_game,
                    background_color=COLOR_PRIMARY,
                    color=COLOR_BACKGROUND,
                    width="100%",
                    margin_top="12px",
                    font_weight="bold",
                ),
                flex="1",
                align_items="start",
                padding="40px",
            ),
            # Right: Dynamic Leaderboard Sidebar
            rx.box(
                rx.vstack(
                    rx.heading("GLOBAL RANKING", size="3", font_family="JetBrains Mono", color="white", letter_spacing="0.2em"),
                    rx.box(height="1px", width="100%", background_color="white", opacity=0.1),
                    rx.vstack(
                        rx.foreach(
                            GameState.leaderboard,
                            lambda entry, index: rx.hstack(
                                rx.text(index + 1),
                                rx.text(entry.initials),
                                rx.spacer(),
                                rx.text(f"{entry.accuracy}%"),
                                width="100%",
                                padding="12px",
                                background_color=rx.cond(index % 2 == 0, "#1c2229", "transparent"),
                                border_left=rx.cond(index == 0, f"2px solid {COLOR_SUCCESS}", "none"),
                            )
                        ),
                        width="100%",
                        spacing="0",
                    ),
                    width="350px",
                    background_color=COLOR_SURFACE,
                    border=f"1px solid {COLOR_SURFACE}",
                    border_radius="12px",
                    overflow="hidden",
                ),
                padding="40px",
            ),
            width="100%",
            height="calc(100vh - 130px)",
            padding_top="80px",
        ),
        footer(),
        height="100vh",
        background_color=COLOR_BACKGROUND,
    )

def leaderboard_view() -> rx.Component:
    return rx.box(
        header(),
        rx.center(
            rx.vstack(
                rx.heading("GLOBAL LEADERBOARD", size="9", font_family="JetBrains Mono", color="white", margin_bottom="20px"),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("RANK"),
                            rx.table.column_header_cell("INITIALS"),
                            rx.table.column_header_cell("ACCURACY"),
                            rx.table.column_header_cell("TIMESTAMP"),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(
                            GameState.leaderboard,
                            lambda entry, index: rx.table.row(
                                rx.table.cell(index + 1),
                                rx.table.cell(entry.initials),
                                rx.table.cell(f"{entry.accuracy}%"),
                                rx.table.cell(entry.timestamp),
                            ),
                        )
                    ),
                    width="100%",
                ),
                rx.button("BACK TO START", on_click=GameState.reset_game, margin_top="40px"),
                width="800px",
                padding="40px",
                background_color=COLOR_SURFACE,
                border_radius="12px",
            ),
            padding_top="120px",
        ),
        footer(),
        height="100vh",
        background_color=COLOR_BACKGROUND,
    )

def index() -> rx.Component:
    return rx.box(
        rx.match(
            GameState.phase,
            (GamePhase.IDLE, idle_view()),
            (GamePhase.PLAYING, playing_view()),
            (GamePhase.VAR_FREEZE, var_freeze_view()),
            (GamePhase.RESULT, result_view()),
            (GamePhase.LEADERBOARD, leaderboard_view()),
            idle_view(),
        ),
        background_color=COLOR_BACKGROUND,
        min_height="100vh",
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&family=Noto+Sans:wght@400;500;700&display=swap",
    ],
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    ),
)
app.add_page(index)
