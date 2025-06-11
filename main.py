import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	# Initialize Pygame
	pygame.init()
	# Create the screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	# Create a clock
	clock = pygame.time.Clock()
	dt = 0

	# groups
	updatable = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawables)
	Asteroid.containers = (updatable, drawables, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawables, shots)

	# create a player
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# create an asteroid field
	asteroid_field = AsteroidField()

	# Main game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		# update the objects
		updatable.update(dt)

		# check for collisions
		# player vs asteroids
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()

		# asteroids vs shots
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot):
					asteroid.split()
					shot.kill()

		# fill the screen with black
		screen.fill((0, 0, 0))

		# draw the objects
		for obj in drawables:
			obj.draw(screen)

		# do this last
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()