from game_config import is_paused
from thread_maid import ThreadMaid
from time import sleep


class EnemiesThread:
	__main_thread = ThreadMaid()

	def __init__(self, enemies):
		print(len(enemies))
		self.__enemies = enemies
		self.__run()

	def __update_enemies_pos(self):
		global is_paused

		while not is_paused:
			for enemy in self.__enemies:
				if not enemy.y_pos_is_limit():
					enemy.update_x_pos()
					enemy.show()
				else:
					del enemy
			sleep(0.5)

	def __run(self):
		self.__main_thread.setup(target=self.__update_enemies_pos)
		self.__main_thread.run()
