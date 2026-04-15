import pygame
import sys
import random

pygame.init()

wid, hei = 800, 600
screen = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("Emoji car game")

White = (255, 255, 255)
green = (0, 255, 0)
pink = (255, 192, 203)
font = pygame.font.SysFont("Segoe UI Emoji", 50)
score = 0
level = 1

pup = [100, 100]
pup_s = font.render("🐶", True, White)
pup_r = pup_s.get_rect(topleft=(pup))
clock = pygame.time.Clock()

def spawn_obstacles(n):
 obs = []
 player_area = pygame.Rect(80, 80, 100, 100) # buffer around start
 for _ in range(n):
    while True:
        r = pygame.Rect(random.randint(50, wid-150), random.randint(50, hei-150),
        random.randint(60,120), random.randint(60,120))
        if r.colliderect(player_area) or any(r.colliderect(o) for o in obs):
            continue
        obs.append(r)
        break
    return obs
 
def spawn_goals(n, obs):
 goals = []
 margin = 30
 for _ in range(n):
    while True:
        g = font.render("🍖", True, White).get_rect(
        topleft=(random.randint(margin, wid-margin-50), random.randint(margin,
hei-margin-50))
 )
        if any(g.colliderect(o) for o in obs):
            continue
        goals.append(g)
        break
    return goals
 
# Initial spawn
obstacles = spawn_obstacles(5)
goals = spawn_goals(3, obstacles)
while True:
 screen.fill(pink)
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
 keys = pygame.key.get_pressed()
 if keys[pygame.K_LEFT] and pup[0] > 0:
 pup[0] -= 5
 if keys[pygame.K_RIGHT] and pup[0] < wid - 50:
 pup[0] += 5
 if keys[pygame.K_UP] and pup[1] > 0:
 pup[1] -= 5
 if keys[pygame.K_DOWN] and pup[1] < hei - 50:
 pup[1] += 5
 pup_r.topleft = (pup)
 screen.blit(pup_s, pup)

 # Draw and check goals
 for g in goals[:]:
    goal_s = font.render("🍖", True, White)
    screen.blit(goal_s, g.topleft)
    if pup_r.colliderect(g):
        goals.remove(g)
        score += 1

 # Draw and check obstacles
 for obs in obstacles:
    pygame.draw.rect(screen, green, obs)
    if pup_r.colliderect(obs):
 # On-screen Game Over popup
    msg = font.render("Game Over! 💥", True, White)
    screen.blit(msg, (wid//2 - msg.get_width()//2, hei//2 - msg.get_height()//2))
    pygame.display.flip()
    pygame.time.delay(1500)
    pygame.quit()
    sys.exit()

 # Level up if all goals collected
 if not goals:
 # On-screen Level Complete popup + reset
    msg = font.render(f"Level {level} Complete! 🏆", True, White)
    screen.blit(msg, (wid//2 - msg.get_width()//2, hei//2 - msg.get_height()//2))
    pygame.display.flip()
    pygame.time.delay(1000)
    level += 1
    obstacles = spawn_obstacles(5 + level*2)
    goals = spawn_goals(3 + level, obstacles)
    pup = [100, 100]
    pup_r.topleft = (pup)

 # Draw score and level
 sco = pygame.font.SysFont("Calibri", 25).render(f"Score: {score}", True, White)
 lev = pygame.font.SysFont("Calibri", 25).render(f"Level: {level}", True, White)
 
 screen.blit(sco, (10, 10))
 screen.blit(lev, (10, 40))
 
 pygame.display.flip()
 clock.tick(60)