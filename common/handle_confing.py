"""
============================
Author:丁琴
Time: 10:44
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""

from configparser import RawConfigParser
import os
from common.handle_path import CONF_DIR



class Handle_Confing(RawConfigParser):
    def __init__(self,filename):
        super().__init__()
        self.read(filename,encoding="utf-8")

conf=Handle_Confing(os.path.join(CONF_DIR,"config.ini"))



if __name__=="__main__":
    conf = Handle_Confing(os.path.join(CONF_DIR, "config.ini"))
    s=conf.get("env","headers_token")


