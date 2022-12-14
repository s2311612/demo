# NOTE: Generated By HttpRunner v4.1.6
# FROM: testcases\in_flow\in_flow_add_test_test.json
import pytest
from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import Parameters
from debugtalk import *

class TestCaseInFlowAddTestTest(HttpRunner):
    @classmethod
    def setup_class(cls):
        sql_delete = "delete inf.*,infi.* from inb_flow as inf  " \
                     "inner join inb_flow_item as infi on  infi.flow_id=inf.id"
        setup_hook_sql(sql_delete)

    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                # "parameters_setting": {
                #     "limit": 7,
                #     "pick_order": "sequential",
                #     "strategies": {
                #         "asnType-asnTypeValue": {
                #             "name": "asn",
                #             "pick_order": "sequential",
                #         },
                #     },
                # },
                 "asnType-asnTypeValue": [["CT", "采退入库"], ["CG", "采购入库"], ["XL", "虚拟入库"], ["SH", "售后入库"], ["LY", "领用归还"],
                                          ["DB", "调拨入库"], ["LJ", "拦截入库"]],
                #"asnType-asnTypeValue": [["CT", "采退入库"]]

                # "putawayType": [1, 2, 3],
                # "unloadRecord": [1, 2, 3],
                # "qualityControl": [1, 2, 3],
            }
        )
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("创建入库流程").variables(
        **{
            "sql_delete": "delete inf.*,infi.* from inb_flow as inf  inner join inb_flow_item as infi on  infi.flow_id=inf.id",
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjEsInVuYW1lIjoiYWRtaW4iLCJ1c2VyT3BlcmF0aW9uIjoyLCJjbGllbnQiOiJQQyIsImlzQWRtaW4iOjEsImFwcENvZGUiOiJXTVMiLCJleHAiOjE2NTgyMTAxMTQzOTcsImJpekdyb3VwQ29kZSI6ImFzdXJhLXdtcy1jbHVzdGVyIn0.o52aRmcZBd3mP3dPJjZA1gU5oRcU8fO9fbF9JirhwYE",
            "remark": "AutoTest_${get_timestamp()}",
            "createOrder": 1,
            "approveOrder": 1,
            "createReceiptTask": 1,
            "receipt": 1,
            "putawayType": "${get_random_number(1,3)}",
            "unloadRecord": "${get_random_number(1,3)}",
            "qualityControl": "${get_random_number(1,3)}"
        }
    )
    teststeps = [
        Step(
            RunRequest("Step1:创建流程")
                # .setup_hook("${setup_hook_sql($sql_delete)}")
                .post("http://test.asura-wms.ruigushop.com/api/asura/wms/web/inb/flow/save")
                .with_headers(
                **{
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "271",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Host": "test.asura-wms.ruigushop.com",
                    "Origin": "http://test.asura-wms.ruigushop.com",
                    "Referer": "http://test.asura-wms.ruigushop.com/static/wms/cfg/inb/flow",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                    "business": "RG20",
                    "token": "${token}",
                }
            )
                .with_json(
                {
                    "approveOrder": "${approveOrder}",
                    "asnType": "${asnType}",
                    "asnTypeValue": "${asnTypeValue}",
                    "createOrder": "${createOrder}",
                    "createReceiptTask": "${createReceiptTask}",
                    "ownerList": [
                        {"ownerId": "28218014516117505", "ownerName": "A货主29"},
                        {"ownerId": "27955950061092865", "ownerName": "测试货主"},
                        {"ownerId": "33281615052488706", "ownerName": "锐锢"},
                        {"ownerId": "1516619885371412482", "ownerName": "锐锢"},
                    ],
                    "putawayType": "${putawayType}",
                    "qualityControl": "${qualityControl}",
                    "receipt": "${receipt}",
                    "remark": "${remark}",
                    "unloadRecord": "${unloadRecord}",
                }
            )
                .validate()
                .assert_equal("status_code", 200, "assert response status code")
                .assert_equal("body.code", "0000000", "assert response body code")
                .assert_equal("body.data", None, "assert response body data")
                .assert_equal("body.msg", "操作成功", "assert response body msg")
        ),
        Step(

            RunRequest("Step2:查询列表")
                .post(
                "http://test.asura-wms.ruigushop.com/api/asura/wms/web/inb/flow/listPage"
            )
                .with_headers(
                **{
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "71",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Host": "test.asura-wms.ruigushop.com",
                    "Origin": "http://test.asura-wms.ruigushop.com",
                    "Referer": "http://test.asura-wms.ruigushop.com/static/wms/cfg/inb/flow",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                    "business": "RG20",
                    "token": "${token}",
                }
            )
                .with_json(
                {
                    "current": 1,
                    "paramsList": [],
                    "queryCode": "wms_inb_flow_list",
                    "size": 50,
                }
            )
                .extract()
                .with_jmespath("body.data.records[-1].id", "request_id")
                .validate()
                .assert_equal("status_code", 200, "assert response status code")
                .assert_equal("body.code", "0000000", "assert response body code")
                .assert_equal("body.msg", "操作成功", "assert response body msg")
        ),
        Step(
            RunRequest("Step3:查询流程")
                .post(
                "http://test.asura-wms.ruigushop.com/api/asura/wms/web/inb/flow/getDetailById"
            )
                .with_headers(
                **{
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "26",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Host": "test.asura-wms.ruigushop.com",
                    "Origin": "http://test.asura-wms.ruigushop.com",
                    "Referer": "http://test.asura-wms.ruigushop.com/static/wms/cfg/inb/flow",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                    "business": "RG20",
                    "token": "${token}",
                }
            )
                .with_json({"id": "${request_id}"})
                # .teardown_hook("${teardown_hook_sql($sql_delete)}")
                .validate()
                .assert_equal("status_code", 200, "assert response status code")
                .assert_equal("body.code", "0000000", "assert response body code")
                .assert_equal("body.msg", "操作成功", "assert response body msg")
                .assert_equal("body.data.putawayType", "${putawayType}","校验上架类型")
                .assert_equal("body.data.unloadRecord", "${unloadRecord}","校验卸货登记")
                .assert_equal("body.data.qualityControl", "${qualityControl}","校验质检登记")
                .assert_equal("body.data.receipt", "${receipt}","校验收货")
                .assert_equal("body.data.remark", "${remark}")
        ),
    ]


if __name__ == "__main__":
    TestCaseInFlowAddTestTest().test_start()
