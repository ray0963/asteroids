import pygame

from constants import *

from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color='white', points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        self.timer = max(self.timer - dt, 0)
    def move(self, dt):
        movement_vector = pygame.Vector2(0, dt * PLAYER_SPEED).rotate(self.rotation)
        self.position += movement_vector

    def shoot(self, dt):
        if self.timer == 0:
            shot_velocity = pygame.Vector2(0, PLAYER_SHOT_SPEED).rotate(self.rotation)
            shot = Shot(self.position.x, self.position.y, radius=SHOT_RADIUS, rotation = self.rotation, velocity=shot_velocity)
            self.timer = PLAYER_SHOOT_COOLDOWN
