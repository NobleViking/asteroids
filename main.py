import pygame

from constants import *
from player import Player

def main():
	# Initialize Pygame
	pygame.init()

	# Create the screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Create a clock
	clock = pygame.time.Clock()
	dt = 0

	# create a player
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# Main game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0, 0, 0))
		player.draw(screen)
		
		# do this last
		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()