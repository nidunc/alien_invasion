from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialise the ship and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship’s exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that’s not moving.
        self.moving_left = False
        self.moving_right = False

    def centre_ship(self) -> None:
        """Centre the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Update the ship’s position based on the movement flags."""
        # Update the ship’s rect value, not the rect itself.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = int(self.x)

    def blitme(self) -> None:
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
