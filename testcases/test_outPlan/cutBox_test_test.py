# NOTE: Generated By HttpRunner v4.1.6
# FROM: har\out_plan\cutBox_test.json
from httprunner import HttpRunner, Config, Step, RunRequest, RunSqlRequest
from httprunner import RunTestCase

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from testcases.test_outPlan.confirmById_test_test import  (
    TestCaseConfirmbyidTest as confirmById,
)

class TestCaseCutboxTest(HttpRunner):

    config = Config("波次切箱")

    teststeps = [
        Step(RunTestCase("完成拣货").call(confirmById).export(*["waveId"])),
        Step(
            RunRequest("")
            .post(
                "http://test.asura-wms.ruigushop.com/api/asura/wms/web/out/wave/cutBox"
            )
            .with_headers(
                **{
                    "Content-Type": "application/json;charset=UTF-8",
                    "bid": "1528936961052135425",
                    "businesscode": "RG20",
                    "businessname": "%E5%8D%8E%E5%8D%97%E6%80%BB%E4%BB%93",
                    "token": "${ENV(token)}",
                    "trace.id": "31a5788f-1e3f-9d9a-812d-d92d23c44f46",
                }
            )
            .with_json({"id": "$waveId"})
            .validate()
            .assert_equal("status_code", 200, "assert response status code")
            .assert_equal("body.msg", "操作成功", "assert response body msg")
        ),
    ]



if __name__ == "__main__":
    TestCaseCutboxTest().test_start()