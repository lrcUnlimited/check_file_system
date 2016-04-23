# -*- coding: UTF-8 -*-
__author__ = 'li'
import MySQLdb
from read_config import config

user = config.get('database', 'db_user')
pwd = config.get('database', 'db_password')
host = config.get('database', 'db_ip')
db = config.get('database', 'db_name')
port = int(config.get('database', 'db_port'))
select_sql = 'select * from filehash'
"""
get data from db

"""


def get_data():
    cnx = MySQLdb.connect(user=user, passwd=pwd, port=port, host=host, db=db, charset="utf8")
    cursor = cnx.cursor()
    d = {}
    try:
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        for row in rows:
            d[row[1]] = row[2]
        return d
    except Exception as err:
        print("query database' failed.")
        print("Error: {}".format(err.msg))
    finally:
        cursor.close()
        cnx.close()


# 保存文件hash值到数据库
def save_file_hash(param):
    try:
        cnx = MySQLdb.connect(user=user, passwd=pwd, port=port, host=host, db=db, charset="utf8")
        cursor = cnx.cursor()
        sql = 'INSERT INTO filehash (filename, filehash) VALUES (%s, %s)'
        cursor.execute(sql, param)
        cnx.commit()
    except  Exception as err:
        print 'error'

    finally:
        cursor.close()
        cnx.close()


