import pygame

from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding_with(self, other_circle) -> bool:
        collision_distance = (self.radius + other_circle.radius) * (1 - COLLISION_LENIENCY)
        distance = self.position.distance_to(other_circle.position)
        return distance <= collision_distance
