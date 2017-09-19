from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_static_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

sql = "insert into web_course_information(announcement_Date,information,url,url_text,information_type,web_id) values(%s,%s,%s,%s,%s,%s)"

root_url = 'http://www.im.ntu.edu.tw/~jtlee/'

def jtleeDB_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    url = root_url + 'db/'

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='leftbar').find_all('p')
    for announcement in announcements[2:10]:
        tmp = announcement.get_text()
        announ_date = tmp[:10]
        announ_title = tmp[13:]
        if announcement.find('a') is not None:
            announ_url = url + announcement.find('a').get('href', '')[2:]
            announ_url_text = announcement.find('a').get_text()
        else:
            announ_url = ''
            announ_url_text = ''
        cur.execute(sql,(announ_date,announ_title,announ_url,announ_url_text,'announcements','034'))

    conn.commit()
    cur.close()
    conn.close()
