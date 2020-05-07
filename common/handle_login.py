"""
============================
Author:丁琴
Time: 11:42
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
from common.handle_confing import conf
from requests import request
import jsonpath

class TestLogin:
    @classmethod
    def testlogin(cls):
        # 准备数据
        url=conf.get("env","url")+"/user/login/"
        data={"username":conf.get("user_data","usernamelogin"),"password":conf.get("user_data","passwordlogin")}
        response=request(method="post",url=url,json=data)
        res=response.json()
        token="JWT"+" "+jsonpath.jsonpath(res,"$..token")[0]
        return token


if __name__=="__main__":
    s=TestLogin.testlogin()
    print(s)


