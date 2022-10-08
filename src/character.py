"""Initialize Pygame"""
import pygame
# pylint: disable=no-member

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = pygame.Color('white')
FPS = 10

# class for dino sprite
class DinoSprite(pygame.sprite.Sprite):
    """Initialize DinoSprite"""
    # pylint: disable=C0303
    # pylint: disable=R0903
    def __init__(self):
        super().__init__()
        #adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('./assets/dino0.png'))
        self.images.append(pygame.image.load('./assets/dino1.png'))

        #index value to get the image from the array
        self.index = 0
        self.image = self.images[self.index]

        # creating a rect at position x,y (15,15) of size (134,134)
        self.rect = pygame.Rect(45, 45, 134, 134)
   
    def update(self):
        """Update the sprite"""
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def jump(self):
        "Jump Up"
        if self.rect.y >= 5:
            self.rect.y -= 10
    def fall(self):
        "Fall Down"
        if self.rect.y <= 45:
            self.rect.y += 10   


def main():
    """Initialize the game"""
    # pylint: disable=R0801
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dino_sprite = DinoSprite()
    group = pygame.sprite.Group(dino_sprite)

    clock = pygame.time.Clock()

    running = True
    jumping = 0
    jumping_counter = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            jumping = True
        if jumping:
            if jumping_counter >= 3:
                dino_sprite.fall()
                jumping = False
                jumping_counter = 0
            else:
                dino_sprite.jump()
                jumping_counter += 1
        else:
            dino_sprite.fall()

        group.update()
        screen.fill(BACKGROUND_COLOR)
        group.draw(screen)
        pygame.display.update()
        clock.tick(10)
if __name__ == "__main__":
    main()
