# -*- encoding=utf8 -*-
__author__ = "lsd"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
touch(Template(r"tpl1546074092173.png", record_pos=(-0.339, -0.237), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546934613612.png", record_pos=(-0.444, -0.143), resolution=(1366, 768)))
sleep(1)

touch(Template(r"tpl1546498999958.png", record_pos=(-0.111, 0.007), resolution=(1366.0, 768.0)))

# 点击菜单中的商品“雪梨汁”
# poco("com.yhbc.tablet:id/ll_goodname").child("android.widget.LinearLayout").child("com.yhbc.tablet:id/tv_name").click()

touch(Template(r"tpl1546499298566.png", record_pos=(0.365, -0.105), resolution=(1366, 768)))
touch(Template(r"tpl1546499359252.png", record_pos=(-0.1, -0.156), resolution=(1366, 768)))
touch(Template(r"tpl1546499369153.png", record_pos=(-0.018, -0.158), resolution=(1366, 768)))
touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))
sleep(2)
# 验证属性是否增加显示
prop=poco("com.yhbc.tablet:id/tv_note").get_text()
assert_equal("+香草+去冰",prop,"属性显示=+香草+去冰")
# 验证购物车中订单总金额是否正确
total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("13.0",total_price,"验证购物车中订单总金额是否=13")
touch(Template(r"tpl1546499457896.png", record_pos=(0.282, 0.221), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546071972568.png", record_pos=(0.313, 0.121), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546072136278.png", record_pos=(0.161, -0.236), resolution=(1366, 768)))

sleep(2.0)
# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.tablet:id/tv_total_price").get_text()
print("order_total_price="+order_total_price)
assert_equal(total_price,order_total_price," 订单详情-验证金额总价是否=13")
