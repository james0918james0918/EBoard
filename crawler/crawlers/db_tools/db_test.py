import pymysql

def fetch_eboard_data(sql):
	connection = pymysql.connect(host='140.112.107.81', port=13306, user='root', passwd='2016sdmtest', db='eboard')
	cur = connection.cursor()

	cur.execute(sql)
	result = cur.fetchall()

	cur.close()
	conn.close()

	return result
