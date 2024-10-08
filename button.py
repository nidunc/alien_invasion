from typing import TYPE_CHECKING

import pygame.font

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game: "AlienInvasion", msg: str) -> None:
        """Initialise button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_colour = (0, 135, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button’s rect object and centre it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg: str) -> None:
        """Turn msg into a rendered image and centre text on the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_colour, self.button_colour
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
