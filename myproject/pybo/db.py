# myproject/pybo/db.py

from pymysql import cursors, connect

db = connect(host='localhost',
             user='root',
             password='1111',
             database='pybo',
             cursorclass=cursors.DictCursor)

# db = connect(host='172.31.98.189',
#              user='root',
#              password='12345',
#              database='community',
#              cursorclass=cursors.DictCursor)