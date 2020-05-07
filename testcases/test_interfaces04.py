"""
============================
Author:丁琴
Time: 15:43
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
"""
============================
Author:丁琴
Time: 11:41
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import unittest
import os
from requests import request
import random
import jsonpath
from common.handle_excel import Handle_Excel
from common.handle_confing import conf
from library.myddt import ddt,data
from common.handle_path import DATA_DIR
from common.handle_logging import my_log
from common.handle_envdata import EnvData,replace_data
from common.handle_db import HandleMysql
from common.handle_login import TestLogin
from common.handle_assert import assert_dict

@ddt
class Test_Interfaces(unittest.TestCase):
    excel=Handle_Excel(os.path.join(DATA_DIR,"cases.xlsx"),"interfaces")
    cases=excel.read_excle()
    db=HandleMysql()

    @classmethod
    def setUpClass(cls):
        # 调用登录获取token
        cls.token=TestLogin.testlogin()
    @data(*cases)
    def test_interfaces(self,case):
        #准备数据
        url=conf.get("env","url")+case["url"]
        method=case["method"]
        # 随机生成一个项目名称，接口名称替换
        projectname=self.random_projectname()
        intername=self.random_intername()
        setattr(EnvData,"projectname",projectname)
        setattr(EnvData, "intername", intername)
        data=eval(replace_data(case["data"]))
        headers = {"Authorization":self.token}
        excepted=eval(replace_data(case["expected"]))
        row_id=case["case_id"]+1
        #发送请求
        response=request(method=method,url=url,json=data,headers=headers)
        res=response.json()
        # 创建项目成功的用例，提取项目id给新建接口用
        if case["title"] == "创建项目成功":
            project_id=str(jsonpath.jsonpath(res,"$..id")[0])
            setattr(EnvData,"project_id",project_id)
        #断言
        try:
            # 调用断言的方法进行断言
            assert_dict(excepted,res)
            # 判断是否需要进行sql校验，如果有sql语句，需要去数据库查询一下是否有一条该项目或者接口的数据
            if case["check_sql"]:
                sql = replace_data(case["check_sql"])
                res_namecount = self.db.find_count(sql)
                self.assertEqual(1, res_namecount)
        except AssertionError as e:
            self.excel.wirte_excel(row=row_id, column=8, value="不通过")
            my_log.error("用例{},{},不通过".format(case["case_id"], case["title"]))
            my_log.debug("预期结果：{}".format(excepted))
            my_log.debug("实际结果：{}".format(res))
            my_log.exception(e)
            # exception将捕获到异常记录到日志中（对应的等级是error）
            # 主动抛出异常
            raise e
        else:
            self.excel.wirte_excel(row=row_id, column=8, value="通过")
            my_log.info("用例{},{},通过".format(case["case_id"], case["title"]))

    #  随机生成一个数据库未注册的项目名称
    @classmethod
    def random_projectname(cls):
        while True:
            randomnum = str(random.randint(0, 10000))
            name = "微信小程序项目"+randomnum
            sql = 'SELECT * FROM test.tb_projects WHERE name="{}"'.format(name,encoding='utf-8')
            res=cls.db.find_count(sql)
            if res==0:
                return name
    #  随机生成一个数据库未注册的接口名称
    @classmethod
    def random_intername(cls):
        while True:
            randomnum = str(random.randint(0, 1000))
            name = "登录接口"+randomnum
            sql = 'SELECT * FROM test.tb_interfaces WHERE name="{}"'.format(name,encoding='utf-8')
            res=cls.db.find_count(sql)
            if res==0:
                return name