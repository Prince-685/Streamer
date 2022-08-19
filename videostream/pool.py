import pymysql as MYSQL
def ConnectionPooling():
    db=MYSQL.connect(host='localhost',port=3306,user='root',passwd='Pratik@123',db="videostream")
    cmd=db.cursor()
    return db,cmd