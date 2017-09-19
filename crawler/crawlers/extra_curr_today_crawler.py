import datetime
from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_extra_curr_today_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

root_url = 'http://activity.osa.ntu.edu.tw'
driverpath = '/Users/liujui-chi/bin/chromedriver'


def getTargets(soup):
    targetTexts = []
    for blocknews in soup:
        tmp = []
        half = blocknews.find('ul', 'cal').find('li').get_text().split('\n')
        title = half[1]
        source = half[2].split('：')[1]
        duration = half[3].split('：')[1]
        comment = blocknews.find('ul', 'cal').find('li').find(string=lambda text:isinstance(text, Comment)).split('<br />')
        if comment[0].split('：')[1][0] != '\t':
            place = comment[0].split('：')[1]
        else:
            place = ''
        if len(comment[1].split('：')) > 1:
            time = comment[1].split('：')[1]
        else:
            time = ''
        tmp.append(title)
        tmp.append(time)
        tmp.append(place)
        tmp.append(source)
        tmp.append(duration)
        targetTexts.append(tmp)
    return targetTexts

def extra_curr_today_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "009", "課指組今日活動", "公告", root_url + "/Calendar")
    '''
        Retruns a list-of-list.
        Inside the list-of-list
            each[0] should bes the announcement date
            each[1] should be the announcement content
            And if link exists
                each[2] should be the complete link
                each[3] should be the text where link sits on
    '''
    url = 'http://activity.osa.ntu.edu.tw/Calendar' #Ntu Lib Open Time
    html = get_extra_curr_today_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    target = soup.find('div', id = "calList").find_all('div', 'blockNews')
    #print(target)
    targetTexts = getTargets(target)
    for each in targetTexts:
        dates = each[4].split("-")
        start_date = dates[0]
        end_date = dates[1]
        cur.execute("insert into web_public_information(Web_ID,Information_Type,Information,Announcement_Date) values('{id}','{type}','{title}','{sd}','{ed}')".format(id = "009", type = "公告", title = each[0], sd = start_date, ed = end_date))
        #print(each)

    conn.commit()
    cur.close()
    conn.close()
