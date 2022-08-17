import os
import yaml

from config.setting import generate_path


class GetYamlData:
    """ 获取 yaml 文件中的数据 """

    def __init__(self, file_dir):
        self.file_dir = file_dir

    def get_yaml_data(self) -> dict:
        """
        获取 yaml 中的数据
        :param: fileDir:
        :return:
        """
        # 判断文件是否存在
        if os.path.exists(self.file_dir):
            data = open(self.file_dir, 'r', encoding='utf-8')
            res = yaml.load(data, Loader=yaml.FullLoader)
        else:
            raise FileNotFoundError("文件路径不存在")
        return res

if __name__ == '__main__':
    abi = GetYamlData(generate_path('data$lml_ylq$a.yaml')).get_yaml_data()
    print(abi)


