# 作者: 苏尛鱼
# 2026年04月24日18时09分14秒
# xxx@qq.com
from data_define import *
from fileReader_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

txtReader = TxtReader(
    "E:\\File\\pre-postgraduation\\postgraduation-AI-study\\1-8 Days to Python from Beginner to Expert\\file\面向对象\\2011年1月销售数据.txt")
jsonReader = JsonReader(
    "E:\\File\\pre-postgraduation\\postgraduation-AI-study\\1-8 Days to Python from Beginner to Expert\\file\面向对象\\2011年2月销售数据JSON.txt")
jan_data: list[Record] = txtReader.file_read()
feb_data: list[Record] = jsonReader.file_read()
data = jan_data + feb_data
data_dict = dict()
for record in data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
# print(data_dict)
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("money￥", y_axis=list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日的销售额"),
    # legend_opts=LegendOpts(
    #     pos_top="2%",
    #     pos_left="center"
    # )

)
bar.render()
