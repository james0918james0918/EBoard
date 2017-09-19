import datetime
from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_dynamic_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

root_url = 'http://activity.osa.ntu.edu.tw'
driverpath = '/Users/liujui-chi/bin/chromedriver'


def getTargets(soup):
    targetTexts = []
    for item in soup:
        tmp = []
        time = item.find('li', 'date').get_text()
        title = item.find('strong').get_text()
        url = item.find('strong').find('a').get('href', '')
        url = root_url + url
        tmp.append(time)
        tmp.append(title)
        tmp.append(url)
        targetTexts.append(tmp)
    return targetTexts


def extra_curr_announ_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "007", "課指組公告", "公告", root_url + "/Announcement")
    '''
        Retruns a list-of-list.
        Inside the list-of-list
            each[0] should be the announcement date
            each[1] should be the announcement content
            And if link exists
                each[2] should be the complete link
                each[3] should be the text where link sits on
    '''
    url = 'http://activity.osa.ntu.edu.tw/Announcement' #Ntu Lib Open Time
    html = get_dynamic_page(url, "CLASS_NAME", "blockNews")
    soup = BeautifulSoup(html, 'html.parser')

    target = soup.find_all('div', 'blockNews')
    targetTexts = getTargets(target)
    for each in targetTexts:
        announ_date = each[0]
        announ_title = each[1]
        announ_url = each[2]
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "007", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print(each)

    conn.commit()
    cur.close()
    conn.close()
