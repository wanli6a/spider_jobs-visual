from pyecharts import Geo
import pandas as pd
import pymysql
import numpy as np
from pyecharts import WordCloud
from pyecharts import Bar
import re
from pyecharts import Pie

conn = pymysql.Connect(host='localhost', user='root', passwd='wanli666', db='job_infos', port=3306, charset='utf8')


def get_data_list():
    global job_title,area,salary,experience,pub_time,edu_background,company,min_salary,max_salary,city,city_count
    min_salary = []
    max_salary = []
    #从数据库读取表的信息
    df = pd.read_sql('select * from job_info', con=conn)
    df_count_area = pd.read_sql("select area, count(area) from job_info group by area ORDER BY COUNT(area) DESC",con=conn)
    citys = df_count_area['area']
    city_num = df_count_area['count(area)']
    city = np.array(citys).tolist()
    city_count = np.array(city_num).tolist()

    # print(city)
    # print(type(city))

    # job_title0 = df['job_title']
    # area0 = df['area']
    # salary0 = df['salary']
    # experience0 = df['experience']
    # pub_time0 = df['pub_time']
    # edu_background0 = df['edu_background']
    # company0 = df['company']
    # # # 用numpy处理，先将dataframe的列转化成数组，再将数组转化成列表
    # job_title = np.array(job_title0).tolist()
    # salary = np.array(salary0).tolist()
    # for sa in salary:
    #     min_sa = re.match('([0-9]{5}|[0-9]{4})\-([0-9]{5}|[0-9]{4})',sa).group(1)
    #     max_sa = re.match('([0-9]{5}|[0-9]{4})\-([0-9]{5}|[0-9]{4})',sa).group(2)
    #     min_salary.append(min_sa)
    #     max_salary.append(max_sa)
    #
    # company = np.array(company0).tolist()
    # area = np.array(area0).tolist()
    # experience = np.array(experience0).tolist()
    # edu_background = np.array(edu_background0).tolist()
    # pub_time = np.array(pub_time0).tolist()

#可视化部分，作出地图，显示数据
def test_geo():
    geo = Geo("爬虫工作岗位在全国的分布情况", "", title_color="#fff",
              title_pos="center", width=1200,
              height=600, background_color='#404a59')


    geo.add("", city, city_count, visual_range=[0, 15],visual_split_number=0.5, visual_text_color="#fff",
            symbol_size=16, is_visualmap=True)
    geo.show_config()
    geo.render('分布情况11111.html')

# visual_range=[0, 20],,tooltip_formatter=geo_formatter,,geo_cities_coords=[0,0]
def word_cloud():
    # wordcloud = WordCloud(width=900, height=400)
    # wordcloud.add("wordcloud",job_title, edu_background, word_size_range=[20, 80],shape='circle')
    # wordcloud.render("wc词云.html")
    bar = Bar("各城市爬虫工作岗位数量")
    bar.add("数量", city, city_count,xaxis_interval=0, xaxis_rotate=40, yaxis_rotate=40,bar_category_gap='45%')
    bar.render("sales and brands22222.html")

    # // 设置主标题与副标题，标题设置居中，设置宽度为900
    pie = Pie("饼状图", "各城市爬虫工作岗位数量", title_pos='center', width=900)
    # // 加入数据，设置坐标位置为【50，50】，上方的colums选项取消显示
    pie.add("数量", city, city_count, center=[60, 50], is_legend_show=False)
    # # // 加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
    # # pie.add("最高", area, max_salary, center=[75, 50], is_legend_show=False, is_label_show=True)
    # # // 保存图表
    pie.render("area and salarylalalal.html")
def main():

    get_data_list()
    # test_geo()
    word_cloud()

if __name__ == "__main__":
    main()