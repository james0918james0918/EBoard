import requests
import random
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

useragents = [
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
    "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
    "Opera/9.20 (Windows NT 6.0; U; en)",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
    "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", # maybe not
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
    "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
    "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
]


driver_path = "/Users/liujui-chi/bin/chromedriver"


selenium_selector = {
    "CSS_SELECTOR": By.CSS_SELECTOR,
    "CLASS_NAME": By.CLASS_NAME,
    "ID": By.ID
}


def get_static_page(url):
    header = {"User-Agent": random.choice(useragents)}
    page = requests.get(url, headers=header)
    page.encoding = "utf-8"
    return page


def get_dynamic_page(url, iden_method, identifier):
    display = Display(visible=0, size=(800, 800))
    display.start()
    #driver = webdriver.Chrome(driver_path)
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((selenium_selector[iden_method], identifier))
        )
        html = driver.page_source
    finally:
        driver.quit()
    display.stop()
    return html


# used by calendar_crawler
def get_calendar_list_page(url, index):
    display = Display(visible=0, size=(800, 800))
    display.start()
    #driver = webdriver.Chrome(driver_path)
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        driver.find_elements_by_css_selector("td[bgcolor='#FEBA2E'] a")[index].click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "thtext"))
        )
        html = driver.page_source
    finally:
        driver.quit()
    display.stop()
    return html


# used by extra_curr_today_crawler
def get_extra_curr_today_page(url):
    display = Display(visible=0, size=(800, 800))
    display.start()
    #driver = webdriver.Chrome(driver_path)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_id("DaySch").click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pages"))
        )
        html = driver.page_source
    finally:
        driver.quit()
    display.stop()
    return html


def try_ceiba_login(url, username, password):
    result = True
    display = Display(visible=0, size=(800, 800))
    display.start()
    #driver = webdriver.Chrome(driver_path)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath("//form[@name='login2']").find_element_by_tag_name('input').click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "p1"))
        )
        element = driver.find_element_by_xpath("//form[@name='p1']")
        element.find_element_by_xpath("//input[@name='user']").send_keys(username)
        element.find_element_by_xpath("//input[@name='pass']").send_keys(password)
        element.find_element_by_xpath("//input[@name='Submit']").click()
    except:
        print("ERROR: Could not log in!")
        result = False
    else:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "wel-msg"))
            )
            targets = driver.find_element_by_id("main").find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
        except:
            print("ERROR: Could not log in!")
            result = False
    finally:
        driver.quit()
    display.stop()
    return result


def get_ceiba_courses(url, username, password):
    courses = []
    display = Display(visible=0, size=(800, 800))
    display.start()
    #driver = webdriver.Chrome(driver_path)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath("//form[@name='login2']").find_element_by_tag_name('input').click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "p1"))
        )
        element = driver.find_element_by_xpath("//form[@name='p1']")
        element.find_element_by_xpath("//input[@name='user']").send_keys(username)
        element.find_element_by_xpath("//input[@name='pass']").send_keys(password)
        element.find_element_by_xpath("//input[@name='Submit']").click()
    except:
        print("ERROR: Could not log in!")
    else:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "wel-msg"))
            )
            targets = driver.find_element_by_id("main").find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
        except:
            print("ERROR: Could not find courses!")
        else:
            for target in targets[1:]:
                target.find_element_by_tag_name('a').click()

            for handle in driver.window_handles[1:]:
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "wel-msg"))
                    )
                except:
                    print("ERROR: Could not find schedule!")
                else:
                    a_course = []

                    driver.switch_to_window(handle)

                    driver.switch_to_frame('Main')
                    driver.switch_to_frame('topFrame')

                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    course_title = soup.find("h1", id="co_name").get_text()
                    a_course.append(course_title)

                    driver.switch_to.default_content()

                    driver.switch_to_frame('Main')
                    driver.switch_to_frame('leftFrame')
                    driver.find_element_by_id('syllabus').find_element_by_xpath('..').click()
                    driver.switch_to_frame('mainFrame')

                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    a_course.append(soup)
                    courses.append(a_course)
    finally:
        driver.quit()
    display.stop()
    return courses
