# 作者: 苏尛鱼
# 2026年04月24日17时17分15秒
# xxx@qq.com
import fileinput
import json

import data_define


class FileReader:
    def file_read(self):
        """
        实现文件的读取功能，抽象类
        :return:
        """
        pass


class TxtReader(FileReader):
    def __init__(self, path):
        self.path = path

    def file_read(self) -> list:
        f = open(self.path, "r", encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            line = line.strip()
            line_list = line.split(",")
            record = data_define.Record(line_list[0], line_list[1], int(line_list[2]), line_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonReader(FileReader):
    def __init__(self, path):
        self.path = path

    def file_read(self) -> list:
        f = open(self.path, "r", encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            dict_line = json.loads(line)
            record = data_define.Record(dict_line["date"], dict_line["order_id"], int(dict_line["money"]),
                                        dict_line["province"])
            record_list.append(record)
        f.close()
        return record_list


if __name__ == '__main__':
    txtReader = TxtReader(
        "E:\\File\\pre-postgraduation\\postgraduation-AI-study\\1-8 Days to Python from Beginner to Expert\\file\面向对象\\2011年1月销售数据.txt")
    print(txtReader.file_read())
    jsonReader = JsonReader(
        "E:\\File\\pre-postgraduation\\postgraduation-AI-study\\1-8 Days to Python from Beginner to Expert\\file\面向对象\\2011年2月销售数据JSON.txt")
    print(jsonReader.file_read())
