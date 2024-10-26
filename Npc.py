import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NPC")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

class NPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 2

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += random.choice([-self.speed, 0, self.speed])
        self.y += random.choice([-self.speed, 0, self.speed])
        self.x = max(0, min(WIDTH - self.width, self.x))
        self.y = max(0, min(HEIGHT - self.height, self.y))

    def check_proximity(self, player_pos):
        if abs(self.x - player_pos[0]) < 50 and abs(self.y - player_pos[1]) < 50:
            return True
        return False

npc = NPC(WIDTH // 2, HEIGHT // 2)
player_pos = (WIDTH // 4, HEIGHT // 4)
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    npc.move()
    npc.draw(screen)

    if npc.check_proximity(player_pos):
        text = font.render("Hola, te doy la bienvenida al SENA, ¿estas listo para comenzar la inducción?", True, (0, 0, 0))
        screen.blit(text, (npc.x, npc.y - 30))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()