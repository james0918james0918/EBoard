from crawlers.activities_crawler import activities_crawler
from crawlers.calendar_crawler import calendar_crawler
from crawlers.extra_curr_announ_crawler import extra_curr_announ_crawler
from crawlers.announ_crawler import *
from crawlers.extra_curr_today_crawler import extra_curr_today_crawler

class AnnounCrawler(object):

	def __init__(self):
		pass

	def get_activities(self):
		return activities_crawler()

	def get_calendar(self):
		return calendar_crawler()

	def get_extra_curr_announ(self):
		return extra_curr_announ_crawler()

	def get_ia(self):
		return ia_crawler()

	def get_ntu_mana_dep(self):
		return ntu_mana_dep_crawler()

	def get_ntuba(self):
		return ntuba_crawler()

	def get_ntuacc(self):
		return ntuacc_crawler()

	def get_ntufin(self):
		return ntufin_crawler()

	def get_ntuib(self):
		return ntuib_crawler()

	def get_ntuim(self):
		return ntuim_crawler()

	def get_ntuemba(self):
		return ntuemba_crawler()

	def get_ntueimba(self):
		return ntueimba_crawler()

	def get_general_affairs(self):
		return general_affairs_crawler()

	def get_ga_doc(self):
		return ga_doc_crawler()

	def get_ga_general(self):
		return ga_general_crawler()

	def get_ga_property(self):
		return ga_property_crawler()

	def get_ga_construction(self):
		return ga_construction_crawler()

	def get_ga_cashier(self):
		return ga_cashier_crawler()

	def get_ga_procurement(self):
		return ga_procurement_crawler()

	def get_ga_facilities_service(self):
		return ga_facilities_service_crawler()

	def get_academic_affairs(self):
		return academic_affairs_crawler()

	def get_student_affairs(self):
		return student_affairs_crawler()

	def get_extra_curr_today(self):
		return extra_curr_today_crawler()
