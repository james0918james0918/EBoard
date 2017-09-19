from crawlers.crawler_tools.static_urls import url_dict
from crawlers.crawler_tools.crawler_helper import get_static_page
from crawlers.db_tools.db_connect import conn_to_db
from crawlers.db_tools.db_connect import website_info_insert
from bs4 import BeautifulSoup

management_root_url = "http://www.management.ntu.edu.tw"

def __getManagementAnnouncements__(soup):
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
    website_info_insert(cur, "008", "管院國際事務室", "公告", management_root_url + "/ia")

    url = management_root_url + "/ia"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "008", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def ntu_mana_dep_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "011", "管理學院首頁", "公告", management_root_url)

    url = management_root_url
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "011", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def ntuba_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "012", "工商管理學系", "公告", management_root_url + "/ba")

    url = management_root_url + "/ba"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "012", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def ntuacc_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "013", "會計學系", "公告", management_root_url + "/acc")

    url = management_root_url + "/acc"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "013", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def ntufin_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "014", "財務金融學系", "公告", management_root_url + "/fin")

    url = management_root_url + "/fin"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "014", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def ntuib_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "015", "國際企業學系", "公告", management_root_url + "/ib")

    url = management_root_url + "/ib"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "").replace("'", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "015", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def ntuim_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "016", "資訊管理學系", "公告", management_root_url + "/im")

    url = management_root_url + "/im"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "016", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def ntuemba_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "017", "高階管理專班", "公告", management_root_url + "/emba")

    url = management_root_url + "/emba"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "017", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def ntueimba_crawler():
    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "018", "創業創新專班", "公告", management_root_url + "/eimba")

    url = management_root_url + "/eimba"
    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id="main-wrapper").find('div', 'span5').find('div', id="home-tab-0").find_all('tr')
    #print(announcements)
    announcementTexts = __getManagementAnnouncements__(announcements)
    for key in announcementTexts:
        announ_date = key
        announ_url = management_root_url + announcementTexts[key][0]
        announ_title = announcementTexts[key][1].replace("\n", "").replace(" ", "")
        cur.execute("insert into web_admin_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "018", type = "公告", url = announ_url, title = announ_title, ad = announ_date))
        #print("%s: %s" % (key, announcementTexts[key]))

    conn.commit()
    cur.close()
    conn.close()

def general_affairs_crawler():
    url = 'http://www.ga.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "019", "總務處公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='main').find('table', 'w-annc__table').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_date = announcement.find('td', 'w-annc__postdate').get_text()
        announ_title = announcement.find('td', 'w-annc_content').find('a').get_text()
        announ_url = announcement.find('td', 'w-annc_content').find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "019", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def ga_doc_crawler():
    url = 'http://doc.ga.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "020", "總務處文書組公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='main').find('table', 'w-annc__table').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_date = announcement.find('td', 'w-annc__postdate').get_text()
        announ_title = announcement.find('td', 'w-annc_content').find('a').get_text()
        announ_url = announcement.find('td', 'w-annc_content').find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "020", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def ga_general_crawler():
    url = 'http://general.ga.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "021", "總務處事務組公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='main').find('table', 'w-annc__table').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_date = announcement.find('td', 'w-annc__postdate').get_text()
        announ_title = announcement.find('td', 'w-annc_content').find('a').get_text()
        announ_url = announcement.find('td', 'w-annc_content').find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "021", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def ga_property_crawler():
    url = 'http://property.ga.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "022", "總務處保管組公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='main').find('table', 'w-annc__table').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_date = announcement.find('td', 'w-annc__postdate').get_text()
        announ_title = announcement.find('td', 'w-annc_content').find('a').get_text()
        announ_url = announcement.find('td', 'w-annc_content').find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "022", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def ga_construction_crawler():
    url = 'http://construction.ga.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "023", "總務處營繕組公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='main').find('table', 'w-annc__table').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_date = announcement.find('td', 'w-annc__postdate').get_text()
        announ_title = announcement.find('td', 'w-annc_content').find('a').get_text()
        announ_url = announcement.find('td', 'w-annc_content').find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "023", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def ga_cashier_crawler():
    url = 'http://cashier.ga.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "024", "總務處出納組公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='main').find('table', 'w-annc__table').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_date = announcement.find('td', 'w-annc__postdate').get_text()
        announ_title = announcement.find('td', 'w-annc_content').find('a').get_text()
        announ_url = announcement.find('td', 'w-annc_content').find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "024", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def ga_procurement_crawler():
    url = 'http://procurement.ga.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "025", "總務處採購組公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='main').find('table', 'w-annc__table').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_date = announcement.find('td', 'w-annc__postdate').get_text()
        announ_title = announcement.find('td', 'w-annc_content').find('a').get_text()
        announ_url = announcement.find('td', 'w-annc_content').find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "025", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def ga_facilities_service_crawler():
    url = 'http://fss.ga.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "026", "總務處經營管理組公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('div', id='main').find('table', 'w-annc__table').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_date = announcement.find('td', 'w-annc__postdate').get_text()
        announ_title = announcement.find('td', 'w-annc_content').find('a').get_text()
        announ_url = announcement.find('td', 'w-annc_content').find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "026", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def academic_affairs_crawler():
    url = 'http://www.aca.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "027", "教務處公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('table', id='table_blue').find('tbody').find_all('tr')
    for announcement in announcements:
        announ_title = announcement.find_all('td')[1].find('a').get_text()
        announ_date = announcement.find_all('td')[-1].get_text()
        announ_url = announcement.find_all('td')[1].find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "027", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()

def student_affairs_crawler():
    url = 'http://osa.ntu.edu.tw'

    conn = conn_to_db()
    cur = conn.cursor()
    website_info_insert(cur, "028", "學務處公告", "公告", url)

    page = get_static_page(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    announcements = soup.find('section', 'content-1').find('tbody').find_all('tr')
    #print(announcements)
    for announcement in announcements:
        announ_title = announcement.find_all('td')[1].find('a').get_text()
        announ_date = announcement.find_all('td')[-1].get_text()
        announ_url = url + announcement.find_all('td')[1].find('a').get('href', '')
        cur.execute("insert into web_public_information(Web_ID,Information_Type,url,Information,Announcement_Date) values('{id}','{type}','{url}','{title}','{ad}')".format(id = "028", type = "公告", url = announ_url, title = announ_title, ad = announ_date))

    conn.commit()
    cur.close()
    conn.close()
