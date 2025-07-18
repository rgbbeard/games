import threading
from ctypes import (pythonapi, py_object)


class ThreadMaid:
	__thread = None
	thread_id = 0
	__thread_target = None
	__thread_arguments = tuple()
	is_running = False

	def __init__(self):
		pass  # Just instantiate the class

	def setup(self, target: object, arguments: tuple = ()):
		self.__set_target(target)
		self.__set_arguments(arguments)
		self.__thread = threading.Thread(target=self.__thread_target, args=self.__thread_arguments)
		self.thread_id = self.__get_id()

		return self

	def __set_target(self, t):
		self.__thread_target = t

	def __set_arguments(self, a: tuple):
		if len(a) > 0:
			self.__thread_arguments = a

	def __get_id(self):
		if hasattr(self.__thread, '_thread_id'):
			return self.__thread._thread_id

		for id, thread in threading._active.items():
			if thread == self:
				return id

	def halt(self):
		if self.__thread != None:
			try:
				thread_stopped = pythonapi.PyThreadState_SetAsyncExc(self.thread_id, py_object(SystemExit))

				if thread_stopped > 1:
					pythonapi.PyThreadState_SetAsyncExc(self.thread_id, 0)

				self.is_running = False

			except Exception as e:
				raise Exception(f"Unable to quit Thread ID: {self.thread_id}")

	def run(self):
		if self.__thread != None:
			self.__thread.start()
			self.is_running = True
