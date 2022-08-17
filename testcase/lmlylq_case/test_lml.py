from decimal import Decimal
from utils.log_utils.logs_utils import *
import allure
import pytest
from utils.other_utils.requests_utils import sendRequest
from utils.read_write_utils.read_yaml import GetYamlData, generate_path

path = GetYamlData(generate_path('data$lml_ylq$a.yaml')).get_yaml_data()


@allure.epic(path['case_common']['allureEpic'])
@allure.feature(path['case_common']['allureFeature'])
class TestLML:
    blocks = "43373"
    hash_s = "0xf115de65c0f107af3f486ba1e318da3b5f987f0998811ffdf05ed5ec608ce7c1"
    address_s = ["0xb304487ac5d6ba6e56429c967faf4989c20599aa", "0x20511bfddb061014ca8839935580c31bdd111c30"]

    @allure.story(path['case_common']['allureStory'])
    @pytest.mark.parametrize("address_s", address_s, ids=address_s)
    def test_address(self, address_s):
        url = "http://ul-wallet.funstars.com.cn/bonusRecords/balance/0x32320115173e865Db96e52e0ece5Bf791deaEb75/" + address_s
        url2 = "https://web3.funstars.com.cn/api/address/" + address_s + "/1/all"
        headers = path['common_data']['headers']
        message = sendRequest(url=url, method="get", headers=headers)
        message2 = sendRequest(url=url2, method="get")
        balance = round(Decimal(message2["data"]["address"]["balance"]) / 1000000000000000000, 6)
        INFO.logger.info("游览器查询余额{}，链查询余额{}".format(str(round(Decimal(message["data"]), 6)), str(balance)))
        assert message["code"] == 200
        assert message["message"] == "查询成功"
        assert round(Decimal(message["data"]), 6) == balance
    # @allure.story("获得照现令产生收益")


if __name__ == '__main__':
    # pytest.main(['test_get_user_info.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
    pytest.main(['test_lml.py', '-s'])
