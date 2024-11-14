

import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        # Initialize the player's attributes
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 5

    def draw(self, surface):
        # Draw the player on the given surface
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dx, dy):
        # Move the player by dx and dy
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    
    def check_collision(self, enemy):
        # Get the rectangles
        rect1 = self.rect
        rect2 = enemy.rect
        
        # Check for overlap on the x-axis
        if rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x:
            # Check for overlap on the y-axis
            if rect1.y < rect2.y + rect2.height and rect1.y + rect1.height > rect2.y:
                return True
        return False

class Enemy:
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self):
        # Simple horizontal movement
        self.rect.x += self.speed
        # Reverse direction at screen edges
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.speed = -self.speed
    

# Initialize Pygame
pygame.init()
# Set up font for displaying text
font = pygame.font.SysFont(None, 74)

# Set up the display
screen_width, screen_height = 640, 480
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Classes in Pygame")

# Create a player instance
player = Player(50, 50, 50, 50, (0, 128, 255))

# Create an enemy instance
enemy = Enemy(100, 200, 50, 50, (255, 0, 0), 3)

# Game loop
running = True
game_active = True  # Game state flag

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handling game logic
    if game_active:
        # Handle key presses
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        player.move(dx, dy)

        # Move enemy
        enemy.move()

        # Check for collision
        if player.check_collision(enemy):
            print("Collision detected!")
            game_active = False  # Stop the game


    # Clear the screen
    window.fill((0, 0, 0))
    


    if game_active:
        # Draw the player and enemy
        player.draw(window)
        enemy.draw(window)
    else:
        # Display "You Died" message
        text = font.render("You Died", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
        window.blit(text, text_rect)

    
    # Update the display
    pygame.display.flip()
    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
