# NOTE: Generated By HttpRunner v4.3.0
# FROM: testcases\test_outPlan\searchId_test.yaml
from httprunner import HttpRunner, Config, Step, RunRequest,RunSqlRequest


class TestCaseSearchidTest(HttpRunner):

    config = (Config("出库订单流程测试").export(*["id", "skuCodes", "usable_qty", "occupy_qty", "picked_qty", "skuQty"])
              .db()
              .user('asura')
              .password("asura")
              .ip("test.mysql8.ruigushop.com")
              .port(3306)
              .database("asura_wms_005"))

    teststeps = [
        Step(
            RunRequest("查询ID")
            .post(
                "http://test.asura-wms.ruigushop.com/api/asura/wms/web/out/plan/listPlanUnClose"
            )
            .with_headers(
                **{
                    "Content-Type": "application/json;charset=UTF-8",
                    "bid": "1528936961052135425",
                    "businesscode": "RG20",
                    "businessname": "%E5%8D%8E%E5%8D%97%E6%80%BB%E4%BB%93",
                    "token": "${ENV(token)}",
                    "trace.id": "3397436d-ea4e-4d74-2dcd-e34c19a83b27",
                }
            )
            .with_json(
                {
                    "current": 1,
                    "extra": {},
                    "paramsList": [
                        {
                            "argValue": "${ENV(plan_no)}",
                            "itemId": "6049",
                            "itemName": "sourceNo",
                        }
                    ],
                    "queryCode": "wms_out_plan_list",
                    "size": 100,
                }
            )
            .extract()
            .with_jmespath("body.data.records[0].id", "id")
            .with_jmespath("body.data.records[0].skuCodes", "skuCodes")
            .with_jmespath("body.data.records[0].skuQty", "skuQty")
            .validate()
            .assert_equal("body.msg", "操作成功", "assert response body msg")
        ),
        Step(
                RunSqlRequest("查询所有库存")
                .fetchone("select * from asura_wms_005.inv_inventory where sku_code = $skuCodes;")
                .extract()
                .with_jmespath("usable_qty", "usable_qty") #可用数量
                .with_jmespath("occupy_qty", "occupy_qty") #占用数量
        ),
        Step(
                RunSqlRequest("查询已拣数量")
                .fetchone("select * from asura_wms_005.inv_inventory where sku_code = $skuCodes and bin_code = 'picking';")
                .extract()
                .with_jmespath("picked_qty", "picked_qty") #已拣数量
        )
    ]


if __name__ == "__main__":
    TestCaseSearchidTest().test_start()
