#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from Code.EnemyShot import EnemyShot
from Code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.speed_y = 2
        self.max_speed_y = self.speed_y
        self.min_speed_y = -self.speed_y * 2

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.name == 'Enemy3':
            self.rect.centery += self.speed_y
            if self.rect.bottom >= WIN_HEIGHT:
                self.rect.bottom = WIN_HEIGHT
                self.speed_y = -self.max_speed_y
            elif self.rect.top <= 0:
                self.rect.top = 0
                self.speed_y = -self.min_speed_y

    def shot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
