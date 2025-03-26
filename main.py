# this allows us to use code from
# the open-source pygame library
# throughout this file
from asteroid import Asteroid
import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0


    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   
    while (True):
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return

         # Clear the screen
         screen.fill((0, 0, 0))  # Fill with black

         updatable.update(dt)
         for asteroid in asteroids:
             if player.collision_check(asteroid):
                 print("Game over")
                 return


         for asteroid in asteroids:
             for bullet in shots:
                 if bullet.collision_check(asteroid):
                     asteroid.split()
                     bullet.kill()

         for obj in drawable:
             obj.draw(screen)
         pygame.display.flip()
         dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

