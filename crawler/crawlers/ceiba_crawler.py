from datetime import datetime
from crawlers.crawler_tools.crawler_helper import get_ceiba_courses
from crawlers.crawler_tools.crawler_helper import try_ceiba_login

def ceiba_crawler(usr, pas):
	url = 'https://ceiba.ntu.edu.tw/index.php'
	list_of_courses = get_ceiba_courses(url, usr, pas)

	today = datetime.today()

	all_courses = {}

	for syllabus in list_of_courses:
		course_name = syllabus[0]
		all_classes = []
		weeks = syllabus[1].find_all("tr")
		start_week = 1
		for i in weeks[1:]:
			ctime = i.find_all("td")[1].get_text().replace(" ", "").split("/")

			formatted_time = datetime(today.year, int(str(ctime[0]).lstrip('0')), int(str(ctime[1]).lstrip('0')))

			print(str(formatted_time.year) + "/" + str(formatted_time.month) + "/" + str(formatted_time.day))

			if formatted_time.month != today.month:
				start_week = start_week + 1
				continue

			if formatted_time.day < today.day:
				start_week = start_week + 1
				continue
			else:
				break

		print(start_week)
		counter = 0
		for t in weeks[start_week:]:
			if counter == 5:
				break
			else:
				a_class = []
				a_class.append(" ".join(t.find_all("td")[1].get_text().split()))
				a_class.append(" ".join(t.find_all("td")[2].get_text().split()))
				file_url = "https://ceiba.ntu.edu.tw/"
				files = {}
				all_files = t.find_all("td")[3].find_all("a")
				for f in all_files:
					files[f.get_text()] = f["href"].replace("../../", file_url)
				a_class.append(files)
				all_classes.append(a_class)
				counter = counter + 1

		all_courses[course_name] = all_classes

	#result = json.dumps(all_courses, ensure_ascii=False).encode('utf8')
	#with open("test.json", 'w', encoding='utf8') as outfile:
	#	json.dump(all_courses, outfile, ensure_ascii=False)
	return all_courses


def trial_crawler(usr, pas):
	url = 'https://ceiba.ntu.edu.tw/index.php'
	return try_ceiba_login(url, usr, pas)
