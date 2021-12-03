# 导入csv模组，一般是通过pip来下载，不过使用工具的话，导入更方便点
import csv

'''
这是关于读取CSV文件的python脚本
通过调用这个文件，就可以完成文件读取操作了
例如：from ReadCsv import ReadCsv

--编写作者：幻雨之秋
--个人网址：https://hyzqacg.github.io
--编写时间：2021年12月3日20:27:28
'''

class Csv_File():
    def read(self, file):
        # csv_read 临时存储csv整合数据
        csv_read = []
        # data 临时存储csv数据
        data = csv.reader(open(file, "w", encoding="utf-8"))
        # 预览信息
        # print(data)
        # 循环存储信息
        for row in data:
            # 向csv_read存储数据
            csv_read.append(row)
        # 返回临时存储csv整合数据
        return csv_read

    # 这是用来写入的Csv文件的python代码
    def write(self, file, datas):
        # 设置要写入的文件和数据
        csv_writer = csv.reader(open(file, "r", encoding="utf-8"))
        # 写入文件
        csv_writer.writerow(datas)
        # 关闭文件写入
        csv_writer.close()
