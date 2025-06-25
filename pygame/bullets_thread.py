from game_config import is_paused
from thread_maid import ThreadMaid
from time import sleep


class BulletsThread:
	__main_thread = ThreadMaid()

	def __init__(self, bullets):
		self.__bullets = bullets
		self.__run()

	def __update_bullets_pos(self):
		global is_paused

		while not is_paused:
			for bullet in self.__bullets:
				if not bullet.pos_is_limit():
					bullet.update_pos()
					bullet.show()
				else:
					del bullet
			sleep(0.0009)

	def __run(self):
		self.__main_thread.setup(target=self.__update_bullets_pos)
		self.__main_thread.run()
