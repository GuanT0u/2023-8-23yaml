# 需要自己封装一个类, 实现mysql的增删改查, pymysql


import pymysql
from common.yaml_config import GetConfig


class MysqlOpreta(object):
    def __init__(self):
        """
        初始化操作，把配置文件中mysql的配置读取并赋值对象属性
        """
        mysql_config = GetConfig().get_mysql_config()
        self.db = mysql_config["db"]
        self.host = mysql_config["host"]
        self.password = str(mysql_config["password"])
        self.port = mysql_config["port"]
        self.user = mysql_config["user"]

        self.connect = None  # 链接对象初始化时候是空
        self.cursor = None  # 游标对象初始化时候是空


    def conn_db(self):
        """
        创建连接对象，创建游标对象
        :return: True/False
        """
        try:
            self.connect = pymysql.connect(user=self.user, db=self.db, host=self.host, password=self.password, port=self.port)
        except Exception as e:
            with open("./log.txt", "a") as log_file:
                log_file.write("数据库连接：. {}".format(e.args[-1]))
            return False

        # 创建游标对象 用连接对象的cursor()
        self.cursor = self.connect.cursor()
        return True

    def conn_close(self):
        """
        关闭链接对象，关闭游标对象
        :return:
        """
        self.connect.close()
        self.cursor.close()
        return True

    def commit(self):
        """
        针对写好的sql，提交操作(只针对，新增，修改，删除)
        :return:
        """
        self.connect.commit()
        return True

    def mysql_query(self, sql):
        """
        查询
        :param sql:
        :return:
        """
        # 第一步，创建连接(能获取到的资源是什么? 1连接对象 2游标对象)
        self.conn_db()
        # 第二步，用游标对象执行一个查询sql
        self.cursor.execute(sql)
        # 第三步，调用fetchall()查询多条数据，fetchone()查询一条数据
        result = self.cursor.fetchall()
        if result == None:
            print("查询数据为空")
            with open("./log.txt", "a") as log_file:
                log_file.write("数据库查询：. {}".format("查询数据为空"))
        else:
            print(result)
        # 第四步，关闭资源
        self.conn_close()
        return True

    def change_commit(self):
        self.connect.commit()

    def insert_updte_delte_sql(self, sql):
        """
        增删改
        :return:
        """
        self.conn_db()  # 先启动

        self.cursor.execute(sql)  # 中间执行的sql
        self.change_commit()  # 点击确定


        self.conn_close()  # 最后关闭


if __name__ == "__main__":
    print(MysqlOpreta().conn_db())
    MysqlOpreta().mysql_query("select * from user")

