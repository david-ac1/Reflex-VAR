📄 PRD: "Reflex VAR" – World Cup 2026 Edition
Project Goal: A high-speed, 2D web-based mini-game for LCS/VCT event booths that tests fan "Pro-Intelligence" using official GRID match data.

1. System Overview
   Tech Stack: React (Vite), Tailwind CSS (using the UI Doc provided), Framer Motion (for VAR animations).

Primary AI Agent: JetBrains Junie (Pair Programming Mode).

Data Source: GRID Open Access API (GraphQL for metadata, REST for Series Events).

Target Device: 1080p Landscape Touchscreen Kiosk.

2. Functional Requirements (The "Junie" Instruction Set)
   A. The "VAR Freeze" Engine
   The core mechanic is a "High-Stakes Pause."

Task for Junie: "Implement a game loop that plays a 2D canvas simulation of a pro-play (X/Y coordinates from GRID). At a specific timestamp (e.g., event_type: 'ability_used'), pause the simulation and trigger a 'VAR OVERLAY' state."

Logic: Junie should set up a gameState reducer to handle: IDLE -> PLAYING -> FREEZE -> INPUT_WAIT -> REVIEW -> RESULT.

B. GRID Data Integration (Mock to Real)
Junie needs to handle the abstraction of complex esports data.

Task for Junie: "Create a GridService.ts that fetches SeriesID metadata. Create a mapping function that converts GRID's position.x and position.y to local canvas coordinates based on the 2026 World Cup pitch/map layout."

Expected Schema:

JSON

{
"event": "ability_cast",
"player": "C9_OXY",
"timestamp": 124500,
"target_coords": { "x": 0.45, "y": 0.78 },
"actual_impact_zone": 0.05
}
C. The "Pro-Intelligence" Calculator
Task for Junie: "Write a utility function calculateProAccuracy(userClick, actualCoord). It must use a distance formula capped at 100. If accuracy > 90%, trigger a 'World-Class' UI state."

3. Implementation Plan (25-Day Sprint)
   Phase 1: Environment & Scaffolding (Days 1–5)
   Junie Prompt: "Scaffold a Vite + React + Tailwind project. Create a .junie/guidelines.md file using the UI documentation provided earlier. Ensure the primary color is #00AEEF and the font is JetBrains Mono."

Goal: A working "Start Screen" that follows the Brand Identity.

Phase 2: Data & Core Loop (Days 6–15)
Junie Prompt: "Build the 2D Game Canvas. Create a mock data set of 5 'Clutch Moments' from VALORANT/LoL. Implement a 'Reflex Click' mechanic where the player must tap the screen during the freeze-frame."

Integration: Use Junie to refine the "VAR Review" animation (Slow-mo zoom on the target).

Phase 3: Leaderboard & "Stitch" Ready (Days 16–22)
Junie Prompt: "Implement a Firebase-backed leaderboard. Add a 'Submit Initials' screen. Ensure the UI is responsive for a 1080p kiosk but stays functional on mobile for QR code scans."

Phase 4: Bonus Polish (Days 23–25)
Junie Prompt: "Review the entire codebase for performance bottlenecks. Generate a feedback.md file documenting where you (Junie) were most helpful—this will be used for the $1,000 feedback prize."

4. UI / Interaction Map (For Google Stitch)
   Home: Large "START CHALLENGE" button + WC 2026 Video Background.

Play: 2D Top-Down map (Pitch/Site). Blue nodes (Cloud9) vs Red nodes (Opponent).

VAR Pause: Screen turns grayscale except for the "Junie" helper. Red "Target Reticle" follows finger.

Score: Large 0–100 number. "JUNIE'S TAKE: You reacted 0.2s slower than OXY."