🛠️ Reflex VAR: Design & Implementation Guidelines
1. Core Visual Language
   All components must align with the "Elite Performance Kiosk" aesthetic: a blend of professional sports broadcasting and technical minimalism.

🎨 Color System (Strict HEX)
Background (Main): #0B0E11 (Midnight Grey).

Surface (Cards/Modals): #161B22 (Pitch Charcoal).

Primary Accent: #00AEEF (Cloud9 Blue) — Use for main CTAs and progress bars.

Secondary Accent: #7B61FF (JetBrains Purple) — Use for Junie AI insights and feedback boxes.

Status Indicators: * Success: #00FF94 (Neon Mint).

Critical/Warning: #FF4D00 (Tangerine Shock).

✍️ Typography
Headlines/Data: JetBrains Mono, Bold.

Body/UI Labels: Noto Sans, Regular/Medium (WC 2026 Standard).

Scaling: All text must be legible from 3–5 feet away. Minimum body size: 18px.

2. Functional Constraints
   Platform: Responsive Web App optimized for 1080p Landscape Kiosk.

Input: Touch-first. Minimum hit targets: 48px x 48px. Avoid hover-only states.

Framework: React + Tailwind CSS. Use Framer Motion for all VAR "freeze" and "overlay" transitions.

3. Implementation Logic
   Game Loop: The app must transition through states: IDLE -> PLAYING -> VAR_FREEZE -> USER_INPUT -> REVIEW -> LEADERBOARD.

Data Handling: Use the GridService.ts to map coordinates from the GRID API to the local canvas.

AI Persona: The Junie mascot must be the "Lead Referee." Junie provides the feedback in the REVIEW state using the secondary purple color scheme.

4. Component Standards
   Glassmorphism: Use backdrop-blur-md and bg-opacity-80 on the VAR Scan overlay.

Borders: Use a consistent 12px corner radius for all cards and interactive elements.

Animations:

VAR Freeze: 0.3s ease-in-out transition to grayscale with a high-contrast neon border.

Success Feedback: Pulsing #00FF94 glow around the target node.