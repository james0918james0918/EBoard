import pymysql

def conn_to_db():
	#connection = pymysql.connect(host='172.10.0.2', port=3306, user='root', passwd='2016sdmtest', db='eboard')
	connection = pymysql.connect(host='140.112.107.81', port=13306, user='root', passwd='2016sdmtest', db='eboard')
	return connection


def website_info_insert(cursor, web_id, web_name, web_type, web_url):
	sql = "insert into website(Web_ID,Web_name,Web_type,Web_URL) values('{id}','{name}','{type}','{url}')".format(id = web_id, name = web_name, type = web_type, url = web_url)
	cursor.execute(sql)
