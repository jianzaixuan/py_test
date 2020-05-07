"""
============================
Author:丁琴
Time: 10:51
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""

import pymysql
from common.handle_confing import conf
class HandleMysql:
    def __init__(self):
        """初始化方法中，连接到数据库"""
        # 建立连接
        self.conn=pymysql.connect(host=conf.get("mysql","host"),
                                  port=conf.getint("mysql","port"),
                                  user=conf.get("mysql","user"),
                                  password=conf.get("mysql","password"),
                                  charset="utf8",
                                  cursorclass=pymysql.cursors.DictCursor
                             )
        # 创建一个游标对象
        self.cur=self.conn.cursor()
    def find_one(self,sql):
        """
        查询sql语句返回一条数据
        :param sql: 查询的sql语句
        :return: 返回查询到的一条数据
        :type sql:str
        """
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()
    def find_all(self,sql):
        """
        查询sql返回的所有数据
        :param sql: 查询的sql
        :return: 查询到的所有数据
        """
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()
    def find_count(self,sql):
        """
         sql语句查询到的数据条数
         :param sql: 查询的sql
         :return:查询到的数据条数
        """
        self.conn.commit()
        res=self.cur.execute(sql)
        return res
    def updata(self,sql):
        """

        :param sql: 增删改的sql语句
        :return:
        """
        self.cur.execute(sql)
        return self.conn.commit()

    def close(self):
        """断开游标，关闭连接"""
        self.cur.close()
        self.con.close()

if __name__=="__main__":
    db=HandleMysql()
    sql="select*from futureloan.member  limit 5"
    res=db.find_count(sql)
    print(type(res))
