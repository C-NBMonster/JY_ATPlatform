# coding:utf-8
'''author:wujunwei'''
import unittest
import requests
from common.logger import Log
from common.testmethod import RunMethod
from common.openpy_excel1 import ParseExcel

class wf_api(unittest.TestCase):
    log = Log()

    def test_login(self):
        u'''测试登录'''
        url = "http://10.10.11.132:8015/api/account/GetToken"
        header = {"Accept": "application/json, text/plain, */*"}
        json_data = {
                     "userId": 666666,
                     "password": "123456",
                     "uuId": "a2ae50611d3258c4"
                      }
        self.log.info("------%s外访app登录：start!---------")
        results = requests.post(url, headers=header, data=json_data , verify=False)
        results=results.json()
        print(results)
        self.log.info("测试结果：%s"%results)
        self.assertEqual(results["message"],"登录成功")
        self.log.info("------pass!---------")

    def test_CY(self):
        u'''测试CY合同贷款申请单'''
        url = "http://10.10.11.132:8015/api/Contract/GetCreditInfo"
        header = {"Accept": "application/json, text/plain, */*"}
        json_data = {
                   "contractNo": 9910554387,
                   "state": "a",
                   "creditType": "CY"
                     }
        self.log.info("------%s外访CY合同申请单：start!---------")
        results = requests.post(url, headers=header, data=json_data , verify=False)
        results=results.json()
        print(results)
        self.log.info("测试结果：%s"%results)
        self.assertEqual(results["message"],"获取合同详情信息成功!")
        self.log.info("------pass!---------")

    def test_SC(self):
        u'''测试SC合同贷款申请单'''
        url = "http://10.10.11.132:8015/api/Contract/GetCreditInfo"
        header = {"Accept": "application/json, text/plain, */*" }
        json_data = {
             "contractNo": "12276330002",
             "state": "a",
             "creditType": "SC"
             }
        self.log.info("------%s外访SC合同申请单：start!---------")
        results = requests.post(url, headers=header, data=json_data , verify=False)
        results=results.json()
        print(results)
        self.log.info("测试结果：%s"%results)
        self.assertEqual(results["message"],"获取合同详情信息成功!")
        self.log.info("------pass!---------")

    def test_SS(self):
        u'''测试SS合同贷款申请单'''
        url = "http://10.10.11.132:8015/api/Contract/GetCreditInfo"
        header = {"Accept": "application/json, text/plain, */*" }
        json_data = {
             "contractNo": "16547870001",
             "state": "a",
             "creditType": "SS"
              }
        self.log.info("------%s外访SS合同申请单：start!---------")
        results = requests.post(url, headers=header, data=json_data , verify=False)
        results=results.json()
        print(results)
        self.log.info("测试结果：%s"%results)
        self.assertEqual(results["message"],"获取合同详情信息成功!")
        self.log.info("------pass!---------")

    def test_SH(self):
        u'''测试SH合同贷款申请单'''
        url = "http://10.10.11.132:8015/api/Contract/GetCreditInfo"
        header = {"Accept": "application/json, text/plain, */*" }
        json_data = {
             "contractNo": "991431964",
             "state": "a",
             "creditType": "SH"}
        self.log.info("------%s外访SH合同申请单：start!---------")
        results = requests.post(url, headers=header, data=json_data , verify=False)
        results=results.json()
        print(results)
        self.log.info("测试结果：%s"%results)
        self.assertEqual(results["message"],"获取合同详情信息成功!")
        self.log.info("------pass!---------")

    def test_SF(self):
        u'''测试SF合同贷款申请单'''
        url = "http://10.10.11.132:8015/api/Contract/GetCreditInfo"
        header = {"Accept": "application/json, text/plain, */*" }
        json_data = {
             "contractNo": "17844041003",
             "state": "a",
             "creditType": "SF"}
        self.log.info("------%s外访SF合同申请单：start!---------")
        results = requests.post(url, headers=header, data=json_data , verify=False)
        results=results.json()
        print(results)
        self.log.info("测试结果：%s"%results)
        self.assertEqual(results["message"],"获取合同详情信息成功!")
        self.log.info("------pass!---------")


    def test_SQ(self):
        u'''测试SQ合同贷款申请单'''
        url = "http://10.10.11.132:8015/api/Contract/GetCreditInfo"
        header = {"Accept": "application/json, text/plain, */*" }
        json_data = {
             "contractNo": "17844041002",
             "state": "a",
             "creditType": "SQ"}
        self.log.info("------%s外访SQ合同申请单：start!---------")
        results = requests.post(url, headers=header, data=json_data , verify=False)
        results=results.json()
        print(results)
        self.log.info("测试结果：%s"%results)
        self.assertEqual(results["message"],"获取合同详情信息成功!")
        self.log.info("------pass!---------")

if __name__ == "__main__":
    unittest.main()
