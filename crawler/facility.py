from crawlers.gym_crawler import gym_crawler
from crawlers.lib_crawler import lib_crawler

class FacilityCrawler(object):

	def __init__(self):
		pass

	def get_lib(self):
		lib_crawler()

	def get_gym(self):
		gym_crawler()
