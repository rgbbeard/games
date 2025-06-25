"""
Minimum Python version 3.x
Using Python version 3.9.9
"""

import pygame
from sys import argv
from gui_class import *
from game_config import *
from bullet_class import Bullet
from enemy_class import Enemy
from bullets_thread import BulletsThread
from enemies_thread import EnemiesThread


def load_image(image: str, convert: bool = False):
	if convert:
		return pygame.image.load(image).convert_alpha()
	return pygame.image.load(image)


pygame.init()
clock = pygame.time.Clock()
clock.tick(30)
window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
background_image = load_image("background3.jpg", True)
player_image = load_image("battleship.png", True)
enemy_image = load_image("enemy.png", True)
bullet_image = load_image("bullet2.png", True)
pygame.display.set_caption("Boh")
favicon = load_image("spaceship.png")
pygame.display.set_icon(favicon)

bullets_main_thread = BulletsThread(bullets_array)
enemies_array = [
]
enemies_main_thread = EnemiesThread(enemies_array)


def k_is_arrow(k):
	return k in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)


def unpause_game(p, e):
	global KEYSYM_ESC, KEYSYM_p

	if e.keysym in KEYSYM_ESC or e.keysym.lower() == KEYSYM_p:
		p.dispose()


def pause_game():
	popup = Window(
		window_name="Pausa",
		window_size="350x200",
		window_appearance=WINDOW_CUSTOM,
		window_buttons=True,
		window_mode=WINDOW_NORMAL,
		window_position=WINDOW_CENTERED
	)
	p = popup.window
	label = tkinter.Label(p, text="Premi 'Esc', 'p' o chiudi questa finestra per tornare al gioco")
	label.pack()
	p.bind("<Key>", lambda e: unpause_game(popup, e))
	popup.display()


def display_player(x, y):
	global window

	window.blit(player_image, (x, y))


def move_player_left():
	global player_x, PLAYER_STEP

	player_x -= PLAYER_STEP

	if player_x <= 50:
		player_x = 50


def move_player_right():
	global player_x, WINDOW_X, PLAYER_STEP

	player_x += PLAYER_STEP

	if player_x >= (WINDOW_X - 50):
		player_x = WINDOW_X - 50


def move_player_forward():
	global player_y, WINDOW_Y, PLAYER_STEP

	player_y -= PLAYER_STEP

	if player_y <= 50:
		player_y = 50


def move_player_backwards():
	global player_y, WINDOW_Y, PLAYER_STEP

	player_y += PLAYER_STEP

	if player_y >= (WINDOW_Y - 50):
		player_y = WINDOW_Y - 50


while not can_quit:
	# Set background color	
	window.fill((30, 30, 30))
	window.blit(background_image, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key == Q_KEY:
			can_quit = True

		if event.type == pygame.KEYDOWN and event.key == P_KEY:
			is_paused = True
			pause_game()
			is_paused = False

		if event.type == pygame.KEYDOWN and event.key == SPACE_KEY:
			bullets_array.append(Bullet(root=window, image=bullet_image, start_x=(player_x+10), start_y=player_y, end_y=10))

		if event.type == pygame.KEYDOWN and k_is_arrow(event.key):

			if event.key == pygame.K_LEFT:
				move_player_left()

			if event.key == pygame.K_RIGHT:
				move_player_right()

			if event.key == pygame.K_UP:
				move_player_forward()

			if event.key == pygame.K_DOWN:
				move_player_backwards()

	display_player(player_x, player_y)
	pygame.display.update()
