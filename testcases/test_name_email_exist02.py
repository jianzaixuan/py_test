"""
============================
Author:丁琴
Time: 17:48
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
"""
============================
Author:丁琴
Time: 15:17
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import unittest
import os
from requests import request
import random
from library.myddt import ddt,data
from common.handle_excel import Handle_Excel
from common.handle_path import DATA_DIR
from common.handle_confing import conf
from common.handle_logging import my_log
from common.handle_db import HandleMysql
from common.handle_envdata import EnvData,replace_data
from common.handle_assert import assert_dict

@ddt
class Test_Name_email_exist(unittest.TestCase):
    excel=Handle_Excel(os.path.join(DATA_DIR,"cases.xlsx"),"name_email_exist")
    cases=excel.read_excle()
    db=HandleMysql()
    @data(*cases)
    def test_name_email_exist(self,case):
        # 准备数据
        # 随机生成一个用户名，保存为类属性
        username=self.random_username()
        setattr(EnvData,"username",username)
        # 随机生成一个email，保存为类属性
        email=self.random_email()
        setattr(EnvData,"email",email)
        url=conf.get("env","url")+replace_data(case["url"])
        method=case["method"]
        # 随机生成的用户名去数据库查询，如果能查到count为1.否则为0，然后替换掉expected中的count
        if case["check_sql"]:
            sql = replace_data(case["check_sql"])
            namecount = self.db.find_count(sql)
            if namecount==0:
                count=0
                setattr(EnvData, "count", str(count))
            else:
                count=1
                setattr(EnvData, "count", str(count))
        # 注册成功的预期结果比对了username，这个username是随机生成的，所以设置了动态参数获取
        case["expected"]=replace_data(case["expected"])
        excepted=eval(case["expected"])
        row_id=case["case_id"]+1

        # 发送请求
        response=request(method=method,url=url)
        res=response.json()

        # 断言
        try:
            # 调用断言的方法进行断言
            assert_dict(excepted,res)
        except AssertionError as e:
            self.excel.wirte_excel(row=row_id, column=7, value="不通过")
            my_log.error("用例{},{},不通过".format(case["case_id"], case["title"]))
            my_log.debug("预期结果：{}".format(excepted))
            my_log.debug("实际结果：{}".format(res))
            my_log.exception(e)
            # exception将捕获到异常记录到日志中（对应的等级是error）
            # 主动抛出异常
            raise e
        else:
            self.excel.wirte_excel(row=row_id, column=7, value="通过")
            my_log.info("用例{},{},通过".format(case["case_id"], case["title"]))




    #  随机生成一用户名
    @classmethod
    def random_username(cls):
        while True:
            randomname = str(random.randint(0, 6000000))
            name = "dingqin" + randomname
            return name

    #  随机生成一个数据库未注册的邮箱
    @classmethod
    def random_email(cls):
        while True:
            randomemail = str(random.randint(0, 999999999))
            add_email=["@qq.com","@163.com","@sina.com"]
            lenth=len(add_email)
            randomname=random.randint(0,lenth-1)
            reg_name= add_email[randomname]
            email = randomemail+reg_name
            sql = 'SELECT * FROM test.auth_user WHERE email="{}"'.format(email,encoding='utf-8')
            res=cls.db.find_count(sql)
            if res==0:
                return email

