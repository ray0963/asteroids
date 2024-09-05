import pygame

from constants import *

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 3

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color='white', center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += dt * self.velocity
