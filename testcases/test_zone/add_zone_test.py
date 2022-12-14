# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\test_zone\add_zone.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from loguru import logger

class TestCaseAddZone(HttpRunner):
    logger.debug("${ENV(token)}")
    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/api/asura/wms/web/bas/zone/save")
            .post("http://test.asura-wms.ruigushop.com/api/asura/wms/web/bas/zone/save")
            .with_headers(
                **{
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Content-Length": "68",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Cookie": "UM_distinctid=18026ab51ba1101-0b06ab1750c982-1734337f-e1000-18026ab51bb9b8",
                    "Host": "test.asura-wms.ruigushop.com",
                    "Origin": "http://test.asura-wms.ruigushop.com",
                    "Referer": "http://test.asura-wms.ruigushop.com/static/wms/setting/zone",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                    "business": "RG28",
                    "token": "${ENV(token)}",
                }
            )
            .with_cookies(
                **{
                    "UM_distinctid": "18026ab51ba1101-0b06ab1750c982-1734337f-e1000-18026ab51bb9b8"
                }
            )
            .with_json(
                {"whesName": "chengduc", "zoneCode": "chengducang", "zoneName": "成都"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.code", "0000000")
            .assert_equal("body.msg", "操作成功")
            .assert_equal("body.data", None)
        ),
    ]


if __name__ == "__main__":
    TestCaseAddZone().test_start()
