import os

# Os system is to prevent some issues the console sometimes have to render the health bar
os.system('')


class HealthBar:
    # Health bar elements
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    # Change the color attribute on the character subclasses to one of these
    colors: dict = {"red": "\033[91m", "purple": "\33[95m", "blue": "\33[34m", "blue2": "\33[36m",
                    "blue3": "\33[96m", "green": "\033[92m", "green2": "\033[32m", "brown": "\33[33m",
                    "yellow": "\33[93m", "grey": "\33[37m", "default": "\033[0m"}

    def __init__(self, entity, length: int, color: str = '', is_colored: bool = True) -> None:
        self.entity = entity
        self.length = length
        self.color = self.colors.get(color) or self.colors['default']
        self.is_colored = is_colored
        self.max_value = entity.max_health
        self.current_value = entity.health

    # Update the health bar
    def update(self) -> None:
        self.current_value = self.entity.health

    # Draw the health bar
    def draw(self) -> None:
        # Get the length of the bar and divide it to fit the current value set to the character's life
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")
