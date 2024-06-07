import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SQUARE_SIZE = 20
FPS = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font for the score
font = pygame.font.SysFont(None, 35)

def draw_grid():
    for x in range(0, WIDTH, SQUARE_SIZE):
        for y in range(0, HEIGHT, SQUARE_SIZE):
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def draw_snake(snake_body):
    for segment in snake_body:
        rect = pygame.Rect(segment[0], segment[1], SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

def draw_food(food_pos):
    rect = pygame.Rect(food_pos[0], food_pos[1], SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(screen, RED, rect)

def get_random_food_position(snake_body):
    while True:
        x = random.randint(0, (WIDTH // SQUARE_SIZE) - 1) * SQUARE_SIZE
        y = random.randint(0, (HEIGHT // SQUARE_SIZE) - 1) * SQUARE_SIZE
        food_pos = (x, y)
        if food_pos not in snake_body:
            return food_pos

def display_score(score):
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, [0, 0])

def main():
    clock = pygame.time.Clock()
    running = True

    # Initial snake setup
    snake_body = [(100, 50), (90, 50), (80, 50)]
    direction = 'RIGHT'
    change_to = direction

    # Initial food position
    food_pos = get_random_food_position(snake_body)
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to
        if direction == 'UP':
            new_head = (snake_body[0][0], snake_body[0][1] - SQUARE_SIZE)
        elif direction == 'DOWN':
            new_head = (snake_body[0][0], snake_body[0][1] + SQUARE_SIZE)
        elif direction == 'LEFT':
            new_head = (snake_body[0][0] - SQUARE_SIZE, snake_body[0][1])
        elif direction == 'RIGHT':
            new_head = (snake_body[0][0] + SQUARE_SIZE, snake_body[0][1])

        snake_body.insert(0, new_head)

        # Debugging statement
        print(f'Snake head: {snake_body[0]}, Food position: {food_pos}')

        # Check if the snake has eaten the food
        if snake_body[0] == food_pos:
            print('Food eaten!')
            score += 1
            food_pos = get_random_food_position(snake_body)
        else:
            snake_body.pop()

        # Check for collisions with the boundaries or itself
        if (snake_body[0][0] < 0 or snake_body[0][0] >= WIDTH or
            snake_body[0][1] < 0 or snake_body[0][1] >= HEIGHT or
            snake_body[0] in snake_body[1:]):
            running = False

        # Draw everything
        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake_body)
        draw_food(food_pos)
        display_score(score)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()