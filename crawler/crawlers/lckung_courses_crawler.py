from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_static_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

sql = "insert into web_course_information(announcement_Date,information,url,information_type,web_id) values(%s,%s,%s,%s,%s)"
root_url = 'http://www.im.ntu.edu.tw/~lckung/courses/'

def lckungPD_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    url = root_url + 'PD16/'

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('section', id='syllabus').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_title = announcement.find_all('td')[-1].get_text()
        announ_date = announcement.find_all('td')[0].get_text()
        announ_url = url + announcement.find_all('td')[1].find('a').get('href', '')
        cur.execute(sql,(announ_date,announ_title,announ_url,'announcements','029'))

    conn.commit()
    cur.close()
    conn.close()

def lckungOR_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    url = root_url + 'OR16/'

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('section', id='syllabus').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_title = announcement.find_all('td')[-1].get_text()
        announ_date = announcement.find_all('td')[0].get_text()
        announ_url = url + announcement.find_all('td')[1].find('a').get('href', '')
        cur.execute(sql,(announ_date,announ_title,announ_url,'announcements','030'))

    conn.commit()
    cur.close()
    conn.close()

def lckungPBC_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    url = root_url + 'PBC16/'

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('section', id='syllabus').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_title = announcement.find_all('td')[-1].get_text()
        announ_date = announcement.find_all('td')[0].get_text()
        announ_url = url + announcement.find_all('td')[1].find('a').get('href', '')
        cur.execute(sql,(announ_date,announ_title,announ_url,'announcements','031'))

    conn.commit()
    cur.close()
    conn.close()

def lckungIE_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    url = root_url + 'IE16/'

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('section', id='syllabus').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_title = announcement.find_all('td')[-1].get_text()
        announ_date = announcement.find_all('td')[0].get_text()
        announ_url = url + announcement.find_all('td')[1].find('a').get('href', '')
        cur.execute(sql,(announ_date,announ_title,announ_url,'announcements','032'))

    conn.commit()
    cur.close()
    conn.close()

def lckungSDA_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    url = root_url + 'SDA16/'

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('section', id='syllabus').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_title = announcement.find_all('td')[-1].get_text()
        announ_date = announcement.find_all('td')[0].get_text()
        announ_url = url + announcement.find_all('td')[1].find('a').get('href', '')
        cur.execute(sql,(announ_date,announ_title,announ_url,'announcements','033'))

    conn.commit()
    cur.close()
    conn.close()
