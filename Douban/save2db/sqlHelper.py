# -*- coding:utf-8 -*-

import pymssql


class MSSQL:
    def __GetConnect(self):
        self.conn = pymssql.connect(
            host=".", user="sa", password="sa", database="douban", charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

# 使用方式
ms = MSSQL()
reslist = ms.ExecQuery("SELECT * FROM Movie")
for i in reslist:
    print(i)

# newsql = "UPDATE dbo.a SET name = '没有1' WHERE test = '2' AND name = '没有'"
# ms.ExecNonQuery(newsql.encode('utf-8'))
