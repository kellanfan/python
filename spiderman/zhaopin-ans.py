# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   zhaopin-ans.py
@Time    :   2020/04/15 19:33:50
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
from pyecharts.charts import Bar
from pyecharts import options as opts
from misc.pg_client import Mypostgres

pg_conn = Mypostgres()
sql = 'select city,counts from (select city, count(1) counts from zhaopin group by city) a order by counts desc limit 20'
results = pg_conn.execute(sql)

citys = []
values = []
for row in results:
    citys.append(row[0])
    values.append(row[1])

c = (
    Bar()
        .add_xaxis(citys)
        .add_yaxis("各城市的招聘数量 Top 20", values)
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(name_rotate=60, name="城市", axislabel_opts={"rotate": 45})
    ).render("拉钩城市招聘图.html")
)