from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_static_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

root_url = "https://info2.ntu.edu.tw/register"

def activities_crawler():
	conn = conn_to_db()
	cur = conn.cursor()
	website_info_insert(cur, "001", "國立臺灣大學-活動報名系統", "公告", root_url)

	act_list_url = "/actionList.aspx"
	act_list_page = get_static_page(root_url + act_list_url)

	soup = BeautifulSoup(act_list_page.text, "html.parser")
	act_list = soup.find("ul", id="ulbox").find_all("li")

	for item in act_list:
		act_name = item.find("h2").get_text()
		act_link = "https://info2.ntu.edu.tw/register" + "/" + item.find_all("a")[1]["href"]
		act_date = item.find("strong", "actTime").get_text().replace(" ", "").split("~")
		act_start_date = act_date[0]
		act_end_date = act_date[1]
		cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,start_date,end_date) values('{id}','{type}','{url}','{name}','{sd}','{ed}')".format(id = "001", type = "公告", url = act_link, name = act_name, sd = act_start_date, ed = act_end_date))

	conn.commit()
	cur.close()
	conn.close()
