from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_static_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

root_url = "http://www.management.ntu.edu.tw"

def getAnnouncements(soup):
    announcementTexts = {}
    for each in soup:
        tmp = []
        time = each.find('td', 'announce_date').find('a').find('span').get_text()
        #url = each.find('a', 'sticky').get('href', '')
        url = each.find_all('td')[1].find('a').get('href', '')
        #content = each.find('a', 'sticky').find('span').get_text()
        content = each.find_all('td')[1].find('a').find('span').get_text()
        tmp.append(url)
        tmp.append(content)
        announcementTexts[time] = tmp
    return announcementTexts

def ia_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "008", "管院國際事務室", "公告", root_url + "/ia")

    url = root_url + "/ia"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = getAnnouncements(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "008", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()
