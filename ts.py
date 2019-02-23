import pymysql

conn = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',passwd = '114665',db = 'mysql')
cursor = conn.cursor()
cursor.execute('SELECT VERSION()')
row = cursor.fetchone()
print('MySQL server version:',row[0])
cursor.close()
conn.close()

