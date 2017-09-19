from crawlers.yktasyDS_crawler import yktasyDS_crawler
from crawlers.yktasyIS_crawler import yktasyIS_crawler
from crawlers.yktasySDM_crawler import yktasySDM_crawler
from crawlers.lckung_courses_crawler import *
from crawlers.jtlee_courses_crawler import jtleeDB_crawler
from crawlers.ceiba_crawler import ceiba_crawler
from crawlers.ceiba_crawler import trial_crawler

class CourseCrawler(object):

	def __init__(self):
		pass

	def get_yktasyDS(self):
		yktasyDS_crawler()

	def get_yktasyIS(self):
		yktasyIS_crawler()

	def get_yktasySDM(self):
		yktasySDM_crawler()

	def get_lckungPD(self):
		lckungPD_crawler()

	def get_lckungOR(self):
		lckungOR_crawler()

	def get_lckungPBC(self):
		lckungPBC_crawler()

	def get_lckungIE(self):
		lckungIE_crawler()

	def get_lckungSDA(self):
		lckungSDA_crawler()

	def get_jtleeDB(self):
		jtleeDB_crawler()

	def get_ceiba(self, acc, pas):
		return ceiba_crawler(acc, pas)

	def try_login(self, acc, pas):
		return trial_crawler(acc, pas)
