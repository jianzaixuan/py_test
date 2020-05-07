"""
============================
Author:丁琴
Time: 14:52
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import  unittest
import datetime
from BeautifulReport import BeautifulReport
from common.handle_logging import my_log
from common.handle_path import CASE_DIR,REPORT_DIR
from common.send_email import send_smg
my_log.info("用例执行开始")

suite=unittest.TestSuite()
loader=unittest.TestLoader()

suite.addTest(loader.discover(CASE_DIR))

br=BeautifulReport(suite)
# 每次生成带时间的新文件报告
# time=datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
# br.report("测试",time+"test_report.html",report_dir=REPORT_DIR)
br.report("测试","test_report.html",report_dir=REPORT_DIR)

my_log.info("用例执行结束")
send_smg()


