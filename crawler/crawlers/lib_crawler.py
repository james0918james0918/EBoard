from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_dynamic_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

root_url = 'http://www.lib.ntu.edu.tw/hours'


def getTargets(soup):
    targetTexts = []
    #month = soup.find('span', id= "timeMonth").get_text()
    #day = soup.find('span', id = "timeDate").get_text()
    #time_period = soup.find('div', id = "timeCardRight").find_all('p')[0].get_text()
    #print(soup.find('div', id = "timeCardRight").find_all('p'))
    avail_time = soup.find('div', id = 'timeCardRight').find_all('p')[1].find('span').get_text()
    split_time = avail_time.split('-')
    #tmp = []
    #tmp.append(month)
    #tmp.append(day)
    #targetTexts.append(tmp)
    #targetTexts.append(time_period)
    return split_time

def lib_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "002", "國立臺灣大學圖書館", "場館", root_url)

    '''
        Retruns a list-of-list.
        Inside the list-of-list
            each[0] should be the announcement date
            each[1] should be the announcement content
            And if link exists
                each[2] should be the complete link
                each[3] should be the text where link sits on
    '''
    url = 'http://www.lib.ntu.edu.tw/hours' #Ntu Lib Open Time
    html = get_dynamic_page(url, "ID", "timeCardLeft01")
    soup = BeautifulSoup(html, 'html.parser')

    target = soup.find('div', id = "containerB")
    targetTexts = getTargets(target)
    cur.execute("insert into web_public_information(Web_ID,Information_Type,start_date,end_date) values('{id}','{type}','{st}','{et}')".format(id = "002", type = "場館", st = targetTexts[0], et = targetTexts[1]))
    #for each in targetTexts:
    #    print(each)
    conn.commit()
    cur.close()
    conn.close()
