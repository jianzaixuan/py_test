"""
============================
Author:丁琴
Time: 9:37
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""

def assert_dict(excepted,res):
    """
    自定义 用来对连个字典进行成员运算断言的方法
    :param expected: 预期结果
    :param res: 实际结果
    :return:
    """
    for key in excepted:
        # 判断键是否存在,键对应的值也相等
        if key in res.keys() and excepted[key] == res[key]:
            # 这个键对应的值是否一致,断言通过
            pass
        else:
            raise AssertionError("断言不通过")

# 注册成功的情况
expected1 = {
    "username": "musenww01"
}

# 实际结果
res1 = {
    "id": 1659,
    "username": "musenww01",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNjU5LCJ1c2VybmFtZSI6Im11c2Vud3cwMSIsImV4cCI6MTU4Njk1MjMzNSwiZW1haWwiOiJtdXNlbjA4ODJAcXEuY29tIn0.ACuGW5kukoQjlv1K6UE-4er3l7vL57wOvdpgiTrxGi4"
}
if __name__=="__main__":
    assert_dict(expected1,res1)