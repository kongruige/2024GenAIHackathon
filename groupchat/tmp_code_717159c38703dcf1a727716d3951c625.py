# snake_game.py

import pygame
import random

# Initialize pygame
pygame.init()

# Game window parameters
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur_x, cur_y = self.get_head_position()
        new_x, new_y = (0, 0)

        if self.direction == pygame.K_UP:
            new_x, new_y = (cur_x, cur_y - CELL_SIZE)
        if self.direction == pygame.K_DOWN:
            new_x, new_y = (cur_x, cur_y + CELL_SIZE)
        if self.direction == pygame.K_LEFT:
            new_x, new_y = (cur_x - CELL_SIZE, cur_y)
        if self.direction == pygame.K_RIGHT:
            new_x, new_y = (cur_x + CELL_SIZE, cur_y)

        self.positions = [(new_x, new_y)] + self.positions[:-1]

    def change_direction(self, direction):
        if direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = direction
        if direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = direction
        if direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = direction
        if direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = direction

# Main game function
def main():
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                snake.change_direction(event.key)

        snake.move()

        window.fill(WHITE)
        for pos_x, pos_y in snake.positions:
            pygame.draw.rect(window, BLACK, (pos_x, pos_y, CELL_SIZE, CELL_SIZE))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()