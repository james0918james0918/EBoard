from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_static_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

sql = "insert into web_course_information(announcement_Date,information,url,url_text,information_type,web_id) values(%s,%s,%s,%s,%s,%s)"

root_url = 'http://www.im.ntu.edu.tw'


def getAnnouncements(soup):
    announcementTexts = []
    for each in soup:
        tmp = []
        time = each.get_text()
        tmp = time.split(':')
        tmp[0] = tmp[0][1:]
        tmp[1] = tmp[1][1:]
        if each.find('a') is not None:
            url = each.find('a').get('href', '')
            url = root_url + url
            urlText = each.find('a').get_text()
            tmp.append(url)
            tmp.append(urlText)
        else:
            tmp.append('')
            tmp.append('')
        #print(tmp)
        announcementTexts.append(tmp)
    return announcementTexts


def yktasyIS_crawler():
    '''
        Retruns a list-of-list.
        Inside the list-of-list
            each[0] should be the announcement date
            each[1] should be the announcement content
            And if link exists
                each[2] should be the complete link
                each[3] should be the text where link sits on
    '''
    conn = conn_to_db()
    cur = conn.cursor()
    url = 'http://www.im.ntu.edu.tw/~tsay/dokuwiki/doku.php?id=courses:is2016:main' #Information Security

    website_info_insert(cur, "004", "IS", "課程", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')
   
    announcements = soup.find_all('div', 'level2')[0].find_all('div', 'li')
    #print(announcements)
    announcementTexts = getAnnouncements(announcements)
    for each in announcementTexts:
      #  print(each)
        cur.execute(sql,(each[0],each[1],each[2],each[3],'announcements','004'))

    conn.commit()
    cur.close()
    conn.close()
