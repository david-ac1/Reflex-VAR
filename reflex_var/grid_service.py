import random

class GridService:
    @staticmethod
    def process_reflex_click(x: int, y: int, target_x: int, target_y: int, tolerance: int = 10):
        """
        Mock-process X/Y coordinate data for a 'Reflex Click' mechanic.
        Returns True if the click is within the tolerance of the target.
        """
        distance = ((x - target_x)**2 + (y - target_y)**2)**0.5
        return distance <= tolerance

    @staticmethod
    def get_random_target(max_x: int = 800, max_y: int = 600):
        return random.randint(0, max_x), random.randint(0, max_y)
