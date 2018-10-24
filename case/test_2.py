from common.logger import Log
import unittest
import requests
import json

class Test_Kuaidi(unittest.TestCase):
    log=Log()
    def setUp(self):
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }

    def find_kdi(self,number,name,zname):
        '''
        number="
        name="zhongtong"
        zname="中通快递"
        '''
        self.url="http://www.zto.com/express/expressCheck.html?txtBill=%s"%(number)
        self.log.info(u"测试url地址：%s"%self.url)

        #第一步发送请求
        r=requests.get(self.url,headers=self.headers,verify=False)
        result=r.json()
        self.log.info(u"获取请求结果：%s"%result)
        #第二步获取结果
        self.log.info(u"获取公司名称：%s"%result["company"])
        #获取data内容
        data=result["data"]
        self.log.info(u"获取data内容:%s"%result["data"])
        #获取已签收状态
        get_result=data[0]["context"]
        self.log.info(u"获取已签收状态:%s"%get_result)

        #断言：测试结果与期望结果对比
        self.assertEqual(zname,result["company"])
        self.assertIn(u"已签收",get_result)

    def test_ztong(self):
        '''测试中通快递，单号：75102044240826'''

        self.log.info("------开始-------")
        number="75102044240826"
        name="zhongtong"
        zname=u"中通快递"
        self.log.info(u"测试单号：%s  快递名称:%s"%(number,zname))
        self.find_kdi(number,name,zname)
        self.log.info("-------pass------")

if __name__=="__main__":
    unittest.main()



