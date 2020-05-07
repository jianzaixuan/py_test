"""
============================
Author:丁琴
Time: 15:32
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import logging
from common.handle_confing import conf
from common.handle_path import LOG_DIR
import os

log_filepath =os.path.join(LOG_DIR,conf.get("log", "filename"))
def collcet_log():
    # 1.创建一个日志收集器
    mylog=logging.getLogger("dingqin")
    # 2.设置日志等级
    mylog.setLevel(conf.get("log","level"))
    # 3.设置输出渠道以及输出渠道的等级(输出到文件)
    output=logging.FileHandler(log_filepath,encoding="utf8")
    output.setLevel(conf.get("log","fh_level"))
    mylog.addHandler(output)
    # 输出到控制台
    # sh = logging.StreamHandler()
    # sh.setLevel(conf.get("log","sh_level"))
    # mylog.addHandler(sh)

    # 4.设置输出格式
    forms=conf.get("log","formats")
    form=logging.Formatter(forms)
    output.setFormatter(form)
    # sh.setFormatter(form)

    return mylog
my_log=collcet_log()
if __name__=="__main__":
    my_log = collcet_log()
