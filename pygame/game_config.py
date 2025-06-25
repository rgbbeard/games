"""
Game configuration
"""

can_quit = False
is_paused = False
display_debug = False
verbose_mode = False
Q_KEY = 113
ESC_KEY = 27
P_KEY = 112
SPACE_KEY = 32
KEYSYM_ESC = ("Escape", "escape")
KEYSYM_p = "p"
KEYSYM_P = "P"
WINDOW_X = 500
WINDOW_Y = 800
PLAYER_SIZE = 24
PLAYER_STEP = 20
player_x = (WINDOW_X / 2) - PLAYER_SIZE
player_y = WINDOW_Y - 50
bullets_array = []
enemies_array = []


def print_debug(message: str):
	if display_debug:
		print(f"[DEBUG] {message}")


def print_verbose(message: str):
	if verbose_mode and display_debug:
		print(f"[VERBOSE] {message}")
