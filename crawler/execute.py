from announ import AnnounCrawler
from course import CourseCrawler
from facility import FacilityCrawler

def get_activities(obj):
	obj.get_activities()


def get_lib(obj):
	obj.get_lib()


def get_yktasySDM(obj):
	obj.get_yktasySDM()


def get_yktasyIS(obj):
	obj.get_yktasyIS()


def get_lckung_courses(obj):
	obj.get_lckungPD()
	obj.get_lckungOR()
	obj.get_lckungPBC()
	obj.get_lckungIE()
	obj.get_lckungSDA()


def get_jtlee_courses(obj):
	obj.get_jtleeDB()


def get_gym(obj):
	obj.get_gym()


def get_calendar(obj):
	obj.get_calendar()


def get_extra_curr_announ(obj):
	obj.get_extra_curr_announ()


def get_management_department(obj):
	obj.get_ia()
	obj.get_ntu_mana_dep()
	obj.get_ntuba()
	obj.get_ntuacc()
	obj.get_ntufin()
	obj.get_ntuib()
	obj.get_ntuim()
	obj.get_ntuemba()
	obj.get_ntueimba()


def get_general_affairs(obj):
	obj.get_general_affairs()
	obj.get_ga_doc()
	obj.get_ga_general()
	obj.get_ga_property()
	obj.get_ga_construction()
	obj.get_ga_cashier()
	obj.get_ga_procurement()
	obj.get_ga_facilities_service()


def get_academic_affairs(obj):
	obj.get_academic_affairs()


def get_student_affairs(obj):
	obj.get_student_affairs()


def get_extra_curr_today(obj):
	obj.get_extra_curr_today()


def get_yktasyDS(obj):
	obj.get_yktasyDS()


def get_ceiba(acc, pas):
	course = CourseCrawler()
	return course.get_ceiba(acc, pas)


def try_login(acc, pas):
	course = CourseCrawler()
	return course.try_login(acc, pas)


def general_crawl(identifier, obj):
	{
		'activities': get_activities,
		'lib': get_lib,
		'yktasy_sdm': get_yktasySDM,
		'yktasy_is': get_yktasyIS,
		'lckung_courses': get_lckung_courses,
		'jtlee_courses': get_jtlee_courses,
		'gym': get_gym,
		'calendar': get_calendar,
		'extra_curr_announ': get_extra_curr_announ,
		'management_department': get_management_department,
		'general_affairs': get_general_affairs,
		'academic_affairs': get_academic_affairs,
		'student_affairs': get_student_affairs,
		'extra_curr_today': get_extra_curr_today,
		'yktasy_ds': get_yktasyDS
	}[identifier](obj)


if __name__ == '__main__':

	announ = AnnounCrawler()
	course = CourseCrawler()
	facility = FacilityCrawler()

	general_crawl('activities', announ)
	general_crawl('lib', facility)
	general_crawl('yktasy_sdm', course)
	general_crawl('yktasy_is', course)
	general_crawl('lckung_courses', course)
	general_crawl('jtlee_courses', course)
	general_crawl('gym', facility)
	general_crawl('calendar', announ)
	general_crawl('extra_curr_announ', announ)
	general_crawl('management_department', announ)
	general_crawl('general_affairs', announ)
	general_crawl('academic_affairs', announ)
	general_crawl('student_affairs', announ)
	general_crawl('extra_curr_today', announ)
	general_crawl('yktasy_ds', course)
