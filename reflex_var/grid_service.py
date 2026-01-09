import random
import requests
import os
from dotenv import load_dotenv

# Explicitly load .env file
load_dotenv()

class GridService:
    # GRID Open Access API Endpoints
    # Note: In a production environment, the API Key would be in an environment variable
    GRID_API_URL = "https://api.grid.gg/open-access/graphql"
    API_KEY = os.getenv("GRID_API_KEY", "DEMO_KEY") # User would provide their actual key
    
    @staticmethod
    def fetch_live_clutch():
        """
        Fetch real telemetry from the GRID Open Access API for a VALORANT event.
        Returns a dictionary with event metadata and target coordinates.
        """
        query = """
        query GetValorantEvents {
            allSeries(first: 5, filter: {title: {contains: "VALORANT"}}) {
                edges {
                    node {
                        id
                        events(first: 10) {
                            type
                            timestamp
                            ... on ValorantEvent {
                                position { x y }
                                player { name }
                            }
                        }
                    }
                }
            }
        }
        """
        
        headers = {
            "Authorization": f"Bearer {GridService.API_KEY}",
            "Content-Type": "application/json"
        }
        
        try:
            # For hackathon demonstration, we check if we have a real key
            if GridService.API_KEY == "DEMO_KEY" or not GridService.API_KEY:
                 raise Exception("Using Demo Key - Falling back to validated Mock Data")
            
            response = requests.post(
                GridService.GRID_API_URL, 
                json={'query': query}, 
                headers=headers,
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            
            # Real parsing logic for GRID GraphQL Response
            series_list = data.get("data", {}).get("allSeries", {}).get("edges", [])
            if not series_list:
                raise Exception("No active series found in GRID API")
            
            # Get a random series and a random event from it
            random_series = random.choice(series_list)["node"]
            events = random_series.get("events", [])
            if not events:
                raise Exception("No events found in selected series")
            
            target_event = random.choice(events)
            
            return {
                "player": target_event.get("player", {}).get("name", "Unknown Pro"),
                "event": target_event.get("type", "Game Event"),
                "timestamp": target_event.get("timestamp", "00:00:00:00"),
                "target_x": target_event.get("position", {}).get("x", 0.5),
                "target_y": target_event.get("position", {}).get("y", 0.5),
                "frame_id": f"GRID-{random_series.get('id', 'LIVE')}",
                "video_url": "https://reflex-var-assets.s3.amazonaws.com/c9_clutch_sample.mp4", # Placeholder for real video mapping
                "is_live": True
            }
        except Exception as e:
            print(f"[GRID_SERVICE] {e}")
            # Fallback to high-fidelity mock data ensuring the kiosk stays functional
            clutches = [
                {"player": "C9_OXY", "event": "OXY Flash", "timestamp": "00:14:22:04", "target_x": 0.45, "target_y": 0.78, "frame_id": "RX-9922-84", "video_url": "https://reflex-var-assets.s3.amazonaws.com/c9_oxy_flash.mp4", "is_live": False},
                {"player": "C9_Xeppaa", "event": "Skye Ult", "timestamp": "00:08:45:12", "target_x": 0.22, "target_y": 0.34, "frame_id": "RX-1102-45", "video_url": "https://reflex-var-assets.s3.amazonaws.com/c9_xeppaa_sky.mp4", "is_live": False},
                {"player": "C9_vanity", "event": "Omen TP", "timestamp": "00:22:10:01", "target_x": 0.67, "target_y": 0.12, "frame_id": "RX-4433-90", "video_url": "https://reflex-var-assets.s3.amazonaws.com/c9_vanity_omen.mp4", "is_live": False}
            ]
            return random.choice(clutches)

    @staticmethod
    def calculate_pro_accuracy(user_click: tuple, actual_coord: tuple):
        """
        Calculate accuracy based on distance between user click and actual event.
        Capped at 100. Formula normalized for 0-1 coordinate space.
        """
        ux, uy = user_click
        ax, ay = actual_coord
        # Euclidean distance
        distance = ((ux - ax)**2 + (uy - ay)**2)**0.5
        # 0.05 distance is roughly 90% accuracy in this scale
        accuracy = max(0, 100 - (distance * 200)) 
        return accuracy
