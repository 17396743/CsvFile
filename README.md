# 读写CSV文件脚本🐮🍺
## 这是关于读写CSV文件的python脚本

通过调用这个文件，就可以完成Csv的文件读取操作了

## ☕操作：

```python
from ReadCsv import Csv_File

class Csvdatas():

  # 读取Csv文件内容
  # 第一个参数是文件名
  datas_one = Csv_File().read("文件名")
  # 输出读取到的数据
  print(datas)
  
  # 写入数据到Csv文件
  datas_two = ['1','2','3']
  # 第一个参数是文件名，第二个是写入的参数
  Csv_File().write("文件名",datas_two)


```

