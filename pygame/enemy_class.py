from thread_maid import ThreadMaid
from time import sleep


class Enemy:
	__x_pos = 0
	__y_pos = 0
	__end_x_pos = 0
	__end_y_pos = 0
	__root = None
	__image = None

	def __init__(self, root, image, start_x: int, start_y: int, end_x: int, end_y: int):
		self.__root = root
		self.__image = image
		self.__x_pos = start_x
		self.__y_pos = start_y
		self.__end_x_pos = end_x
		self.__end_y_pos = end_y

	def y_pos_is_limit(self):
		return self.__end_y_pos == self.__y_pos

	def x_pos_is_limit(self):
		return self.__end_x_pos == self.__x_pos

	def update_x_pos(self):
		self.__x_pos += 20

		if self.__x_pos == self.__end_x_pos:
			self.__update_y_pos()

	def __update_y_pos(self):
		self.__y_pos += 20

	def show(self):
		self.__root.blit(self.__image, (self.__x_pos, self.__y_pos))
	