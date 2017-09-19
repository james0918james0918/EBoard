from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_static_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

#root_url = "http://ntusportscenter.ntu.edu.tw/front"
root_url = url_dict["gym_url"]

def get_regular_open_time(soup):
	regular_time = soup.find_all("table", id="Table10")[1].find_all("td")
	time_list = []
	count = 2
	while (count < 8):
		time = regular_time[count].get_text().replace("至", "~") + " " + "".join(regular_time[count + 1].get_text().split()).replace("至", "~")
		time_list.append(time)
		count+=2
	return time_list


def get_news(soup):
	all_news = soup.find_all("table", id="Table11")
	news_list = []
	for item in all_news:
		temp_list = []

		news_title = item.find("a").get_text()
		temp_link = item.find("a")["onclick"]
		start_index = temp_link.index("shownews.aspx")
		end_index = start_index
		while(temp_link[end_index] != '\''):
			end_index = end_index + 1
		news_link = root_url + temp_link[start_index:end_index]

		temp_list.append(news_title)
		temp_list.append(news_link)
		news_list.append(temp_list)
	return news_list


def gym_crawler():
	conn = conn_to_db()
	cur = conn.cursor()
	website_info_insert(cur, "005", "台大綜合體育館", "場館", root_url)

	regular_time_url = "/document_2_1.aspx"
	regular_time_page = get_static_page(root_url + regular_time_url)

	regular_time_soup = BeautifulSoup(regular_time_page.text, "html.parser")
	regular_time_list = get_regular_open_time(regular_time_soup)

	for item in regular_time_list:
		cur.execute("insert into web_public_information(Web_ID,Information_Type,Information) values('{id}','{type}','{title}')".format(id = "005", type = "場館", title = item))

	news_url = "/news.aspx"
	news_page = get_static_page(root_url + news_url)

	news_soup = BeautifulSoup(news_page.text, "html.parser")
	news_list = get_news(news_soup)

	for item in news_list:
		cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information) values('{id}','{type}','{url}','{title}')".format(id = "005", type = "場館", url = item[1], title = item[0]))

	conn.commit()
	cur.close()
	conn.close()
