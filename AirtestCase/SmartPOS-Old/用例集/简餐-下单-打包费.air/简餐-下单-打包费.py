# -*- encoding=utf8 -*-
# 简餐验证增加打包费
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
# touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546074092173.png", record_pos=(-0.339, -0.237), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546934613612.png", record_pos=(-0.444, -0.143), resolution=(1366, 768)))
sleep(1)

touch(Template(r"tpl1546071853905.png", record_pos=(-0.224, 0.01), resolution=(1366, 768)))
touch(Template(r"tpl1546071874112.png", record_pos=(0.252, -0.144), resolution=(1366, 768)))
assert_exists(Template(r"tpl1546071908607.png", record_pos=(0.354, -0.085), resolution=(1366, 768)), "验证下单打包费是否已增加")
# 验证购物车中订单金额是否正确
total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("21.0",total_price,"验证商品+打包费金额是否=21")

touch(Template(r"tpl1546071932023.png", record_pos=(0.283, 0.222), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546071972568.png", record_pos=(0.313, 0.121), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546072136278.png", record_pos=(0.161, -0.236), resolution=(1366, 768)))

sleep(2.0)
# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.tablet:id/tv_total_price").get_text()
print("order_total_price="+order_total_price)
assert_equal(total_price,order_total_price," 订单详情-验证金额总价是否=21")

