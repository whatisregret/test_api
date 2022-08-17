import os
from utils.log_utils.logs_utils import INFO, ERROR
import pytest
from config.setting import ConfigHandler

try:
    INFO.logger.info(
        """
        杜甫-------------------------------------------------登高
        The wind was swift and high, and the apes crowed very sad, and the birds were circling in the white sand of the white sand.
        The endless trees rustle the fallen leaves, the Yangtze river is not expected to roll in the Pentium.
        Sad to Li autumn scenery, the perennial wanderer, life in the disease ridden today alone on the high platform.
        After going through hardships and bitter hatred, the white hair was full of hair, and the waning of the wine glass cup was suspended.
        
        2102-4131

        开始执行{}项目...
        
        """.format("api_ui_test")
    )
    pytest.main(['-s', "-W", 'ignore:Module already imported:pytest.PytestWarning',
                 '--alluredir', './report/tmp', "--clean-alluredir"])
    os.system(r"allure generate ./report/tmp -o ./report/html --clean")
    os.system(f"allure serve ./report/tmp -h 192.168.1.154 -p 9999")
except Exception as e:
    ERROR.logger.error(e)
