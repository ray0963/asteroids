import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation, velocity):
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color='red', center=self.position, radius=self.radius, width=4)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += dt * self.velocity
