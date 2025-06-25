class Bullet:
	__x_pos = 0
	__y_pos = 0
	__end_y_pos = 0
	__root = None
	__image = None

	def __init__(self, root, image, start_x: int, start_y: int, end_y: int = 0):
		self.__image = image
		self.__root = root
		self.__x_pos = start_x
		self.__y_pos = start_y
		self.__end_y_pos = end_y

	def pos_is_limit(self):
		return self.__y_pos <= self.__end_y_pos

	def update_pos(self):
		self.__y_pos -= 4

	def show(self):
		self.__root.blit(self.__image, (self.__x_pos, self.__y_pos))
