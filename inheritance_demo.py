import pygame
import sys,random, math

class Square(pygame.sprite.Sprite):
    #Constructor - Used to create objects of the class
    def __init__(self):
        super(Square,self).__init__()
        self.radius = random.randint(20,50)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),200)
        # All classes inheriting from the Sprite class must have an attribute self.image and self.rect
        self.image = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA)
        self.image.fill(self.color)
        self.rect = self.generate_unique_position()

        self.id = id
        self.deltax = random.choice([-2,-1,1,2])

    def move(self):
        if self.rect.left<0 or self.rect.right>1000 or pygame.sprite.spritecollide(self,squares, False,lambda sprite1, sprite2: sprite1 != sprite2 and sprite1.rect.colliderect(sprite2.rect)):
            self.deltax *= -1

        self.rect.centerx += self.deltax

    def generate_unique_position(self):
        """Generate a position for the square that does not overlap with others."""
        max_attempts = 100  # Limit attempts to avoid infinite loops
        while True:
            # Randomly generate a position for the square
            rect = self.image.get_rect(center=(random.randint(100, 900), random.randint(25, 575)))
            
            # Check for collisions with existing squares
            if not any(rect.colliderect(existing.rect) for existing in squares):
                return rect  # No collision, return this rect



# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("INHERITANCE DEMO")


# Create clock to later control frame rate
clock = pygame.time.Clock()

squares = pygame.sprite.Group()

for i in range(25):
    squares.add(Square())



# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    screen.fill("light blue")
 
    #iterates across group and applies the move method to each individual triangle object
    for sq in squares:
        sq.move()

    # Blit squares
    squares.draw(screen)

    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()
