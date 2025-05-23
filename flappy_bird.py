import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Game constants
GRAVITY = 0.15  # Reduced for smoother gravity
FLAP_STRENGTH = -5  # Adjusted for smoother movement
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds
GROUND_HEIGHT = 100
SCROLL_SPEED = 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
SKY_BLUE = (135, 206, 235)

# Get the screen info for fullscreen
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 40)  # Increased font size for fullscreen

# Bird class
class Bird:
    def __init__(self):
        self.x = SCREEN_WIDTH // 4
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.width = 50
        self.height = 40
        self.alive = True
    
    def flap(self):
        self.velocity = FLAP_STRENGTH
    
    def update(self):
        # Apply gravity with smoother physics
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Keep bird on screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        
        # Check if bird hits the ground
        if self.y + self.height > SCREEN_HEIGHT - GROUND_HEIGHT:
            self.y = SCREEN_HEIGHT - GROUND_HEIGHT - self.height
            self.alive = False
    
    def draw(self):
        # Draw a more detailed bird
        # Body
        pygame.draw.ellipse(screen, (255, 255, 0), (self.x, self.y, self.width, self.height))
        # Eye
        pygame.draw.circle(screen, WHITE, (self.x + 35, self.y + 15), 10)
        pygame.draw.circle(screen, BLACK, (self.x + 38, self.y + 15), 5)
        # Beak
        pygame.draw.polygon(screen, (255, 165, 0), [(self.x + 50, self.y + 20), 
                                                   (self.x + 60, self.y + 15), 
                                                   (self.x + 50, self.y + 25)])

# Pipe class
class Pipe:
    def __init__(self):
        self.gap_y = random.randint(200, SCREEN_HEIGHT - GROUND_HEIGHT - 200)
        self.x = SCREEN_WIDTH
        self.width = 80
        self.passed = False
        self.color = (0, 150, 0)  # Slightly brighter green
    
    def update(self):
        self.x -= SCROLL_SPEED
    
    def draw(self):
        # Draw top pipe with cap
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.gap_y - PIPE_GAP // 2))
        pygame.draw.rect(screen, (0, 100, 0), (self.x - 5, self.gap_y - PIPE_GAP // 2 - 20, self.width + 10, 20))
        
        # Draw bottom pipe with cap
        bottom_pipe_y = self.gap_y + PIPE_GAP // 2
        bottom_pipe_height = SCREEN_HEIGHT - bottom_pipe_y - GROUND_HEIGHT
        pygame.draw.rect(screen, self.color, (self.x, bottom_pipe_y, self.width, bottom_pipe_height))
        pygame.draw.rect(screen, (0, 100, 0), (self.x - 5, bottom_pipe_y, self.width + 10, 20))
    
    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
        
        # Top pipe
        top_pipe = pygame.Rect(self.x, 0, self.width, self.gap_y - PIPE_GAP // 2)
        
        # Bottom pipe
        bottom_pipe = pygame.Rect(self.x, self.gap_y + PIPE_GAP // 2, 
                                 self.width, SCREEN_HEIGHT - (self.gap_y + PIPE_GAP // 2))
        
        return bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe)

# Game functions
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def draw_ground():
    # Draw ground with texture
    ground_y = SCREEN_HEIGHT - GROUND_HEIGHT
    pygame.draw.rect(screen, (101, 67, 33), (0, ground_y, SCREEN_WIDTH, GROUND_HEIGHT))
    
    # Draw grass on top of the ground
    pygame.draw.rect(screen, (76, 153, 0), (0, ground_y, SCREEN_WIDTH, 15))
    
    # Draw some texture lines on the ground
    for i in range(0, SCREEN_WIDTH, 30):
        pygame.draw.line(screen, (90, 60, 30), (i, ground_y + 30), (i + 15, ground_y + 50), 2)
        pygame.draw.line(screen, (110, 70, 40), (i + 15, ground_y + 60), (i + 30, ground_y + 80), 2)

def draw_background():
    # Create a gradient sky
    for y in range(0, SCREEN_HEIGHT - GROUND_HEIGHT):
        # Gradient from lighter blue at top to darker blue at bottom
        color_value = max(100, 235 - int(y * 0.2))
        pygame.draw.line(screen, (135, 206, color_value), (0, y), (SCREEN_WIDTH, y))
    
    # Draw some clouds
    cloud_positions = [(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.1), 
                       (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.2),
                       (SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.15),
                       (SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.3)]
    
    for pos in cloud_positions:
        x, y = pos
        # Draw a fluffy cloud with multiple circles
        pygame.draw.ellipse(screen, WHITE, (x, y, 120, 60))
        pygame.draw.ellipse(screen, WHITE, (x + 30, y - 20, 80, 60))
        pygame.draw.ellipse(screen, WHITE, (x + 70, y, 100, 50))

def show_start_screen():
    draw_background()
    draw_ground()
    
    # Title with shadow effect
    draw_text("FLAPPY BIRD", pygame.font.SysFont('Arial', 60, bold=True), (50, 50, 50), 
              SCREEN_WIDTH // 2 - 170, SCREEN_HEIGHT // 3 + 2)
    draw_text("FLAPPY BIRD", pygame.font.SysFont('Arial', 60, bold=True), (255, 215, 0), 
              SCREEN_WIDTH // 2 - 172, SCREEN_HEIGHT // 3)
    
    # Instructions
    draw_text("Press SPACE to start", font, BLACK, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2)
    draw_text("Press ESC to quit", font, BLACK, SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 50)
    
    # Draw a bird on the start screen
    bird_x = SCREEN_WIDTH // 2 - 25
    bird_y = SCREEN_HEIGHT // 3 - 80
    pygame.draw.ellipse(screen, (255, 255, 0), (bird_x, bird_y, 50, 40))
    pygame.draw.circle(screen, WHITE, (bird_x + 35, bird_y + 15), 10)
    pygame.draw.circle(screen, BLACK, (bird_x + 38, bird_y + 15), 5)
    pygame.draw.polygon(screen, (255, 165, 0), [(bird_x + 50, bird_y + 20), 
                                               (bird_x + 60, bird_y + 15), 
                                               (bird_x + 50, bird_y + 25)])
    
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def show_game_over_screen(score):
    # Keep the background and ground visible
    
    # Semi-transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))  # Black with alpha
    screen.blit(overlay, (0, 0))
    
    # Game over text with shadow
    draw_text("GAME OVER", pygame.font.SysFont('Arial', 60, bold=True), (50, 50, 50), 
              SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 3 + 2)
    draw_text("GAME OVER", pygame.font.SysFont('Arial', 60, bold=True), (255, 0, 0), 
              SCREEN_WIDTH // 2 - 162, SCREEN_HEIGHT // 3)
    
    # Score with highlight
    draw_text(f"Score: {score}", pygame.font.SysFont('Arial', 50), (255, 215, 0), 
              SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 30)
    
    # Instructions
    draw_text("Press SPACE to restart", font, WHITE, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50)
    draw_text("Press ESC to quit", font, WHITE, SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 100)
    
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main_game():
    bird = Bird()
    pipes = []
    score = 0
    last_pipe = pygame.time.get_ticks() - PIPE_FREQUENCY
    game_active = True
    
    while True:
        clock.tick(120)  # Increased frame rate for smoother animation
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird.flap()
                if event.key == pygame.K_ESCAPE:  # Allow escape key to exit fullscreen
                    pygame.quit()
                    sys.exit()
        
        # Draw background
        draw_background()
        
        # Generate pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > PIPE_FREQUENCY and game_active:
            pipes.append(Pipe())
            last_pipe = time_now
        
        # Update and draw pipes
        for pipe in pipes:
            pipe.update()
            pipe.draw()
        
        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if pipe.x > -pipe.width]
        
        # Draw ground
        draw_ground()
        
        # Update and draw bird
        if game_active:
            bird.update()
        bird.draw()
        
        # Check for collisions
        for pipe in pipes:
            if pipe.collide(bird):
                game_active = False
                bird.alive = False
            
            # Check for score
            if pipe.x + pipe.width < bird.x and not pipe.passed and game_active:
                pipe.passed = True
                score += 1
        
        # Check if bird is alive
        if not bird.alive:
            game_active = False
        
        # Display score
        draw_text(f"Score: {score}", font, BLACK, 20, 20)
        
        pygame.display.update()
        
        # If game over, show game over screen
        if not game_active and not any(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE for event in pygame.event.get()):
            pygame.time.delay(1000)  # Small delay before showing game over screen
            show_game_over_screen(score)
            return  # Return to start screen after game over

# Main game loop
while True:
    show_start_screen()
    main_game()
