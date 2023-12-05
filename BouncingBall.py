import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60
BALL_RADIUS = 20

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TikTok Bouncing Ball")

# Create the rectangle the ball will bounce in 
rectangle_width, rectangle_height = 500, 300
rectangle_x, rectangle_y = (WIDTH - rectangle_width) // 2, (HEIGHT - rectangle_height) // 2
#pygame.draw.rect(screen, (255, 0, 0), (rectangle_x, rectangle_y, rectangle_width, rectangle_height))


# Set up the clock
clock = pygame.time.Clock()

# Ball properties
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [5, 5]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off walls and increase speed
    if ball_pos[0] - BALL_RADIUS <= 0 or ball_pos[0] + BALL_RADIUS >= WIDTH:
    #if ball_pos[0] - BALL_RADIUS <= 0 or ball_pos[0] + BALL_RADIUS >= rectangle_width:
        if ball_speed[0] < 0:
            ball_speed[0] = -(ball_speed[0]-1)
        elif ball_speed[0] > 0:
            ball_speed[0] = -(ball_speed[0]+1)

    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
    #if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= rectangle_height:    
        if ball_speed[1] < 0:
            ball_speed[1] = -(ball_speed[1]-1)
        elif ball_speed[1] > 0:
            ball_speed[1] = -(ball_speed[1]+1)

    # Fill the screen with the background color
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, BLUE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    #draw the rectangle
    #pygame.draw.rect(screen, (255, 0 ,0), (rectangle_x, rectangle_y, rectangle_width, rectangle_height), 10)


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
