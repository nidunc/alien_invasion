import json
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.path = Path("extra/high_score.json")
        self.high_score = self.get_stored_highscore()

    def get_stored_highscore(self) -> int:
        """Get stored highscore if available."""
        if self.path.exists():
            contents = self.path.read_text()
            highscore = int(json.loads(contents))
            return highscore
        else:
            return 0

    def store_highscore(self):
        """Store the highscore."""
        contents = json.dumps(self.high_score)
        self.path.write_text(contents)

    def reset_stats(self) -> None:
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
