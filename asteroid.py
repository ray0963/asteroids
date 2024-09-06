import pygame
import random

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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_change = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position.x, self.position.y, radius=self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity.rotate(angle_change) * ASTEROID_SPEEDUP
        asteroid2 = Asteroid(self.position.x, self.position.y, radius=self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = self.velocity.rotate(-angle_change) * ASTEROID_SPEEDUP
