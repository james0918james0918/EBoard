import datetime
from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_dynamic_page
from crawlers.crawler_tools.crawler_helper import get_calendar_list_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

#root_url = "https://ann.cc.ntu.edu.tw/activities/"

root_url = url_dict["calendar_url"]


def calendar_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "006", "台大日曆今日活動", "公告", root_url)

    calendar_page = get_dynamic_page(root_url, "CSS_SELECTOR", "td[bgcolor='#FEBA2E']")

    soup = BeautifulSoup(calendar_page, "html.parser")
    num = len(soup.find("td", bgcolor="#FEBA2E").find_all("span", "text"))

    counter = 0
    while (counter < num):
        list_page = get_calendar_list_page(root_url, counter)
        list_soup = BeautifulSoup(list_page, "html.parser")
        info = list_soup.find_all("td", "nstext")

        info_counter = 1
        while (info_counter < len(info)):
            act_title = info[info_counter].get_text()
            act_date = info[info_counter + 1].get_text().split("-")
            act_start_date = datetime.datetime.strptime(act_date[0], "%m/%d/%Y").strftime("%Y/%m/%d")
            act_end_date = datetime.datetime.strptime(act_date[1], "%m/%d/%Y").strftime("%Y/%m/%d")
            info_counter = info_counter + 5
            cur.execute("insert into web_public_information(Web_ID,Information_Type,Information,start_date,end_date) values('{id}','{type}','{name}','{sd}','{ed}')".format(id = "006", type = "公告", name = act_title, sd = act_start_date, ed = act_end_date))

        counter = counter + 1

    conn.commit()
    cur.close()
    conn.close()
