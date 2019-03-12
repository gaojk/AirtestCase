# -*- encoding=utf8 -*-
# 场景五：到店点餐点“焦糖奶茶-中杯+1元香草”，“波霸奶茶+价格-1”、下单，退一个“焦糖奶茶-中杯+1元香草”，改为“炸鸡腿（称重）+打包”，菜品上齐结账，和商家协商抹零操作，现金-找零，结账后查看宝报表
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
stop_app("com.yhbc.tablet")
start_app("com.yhbc.tablet",activity=None)
touch(Template(r"tpl1550659223584.png", record_pos=(0.305, -0.063), resolution=(1366, 768)))
sleep(10)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
# 点餐操作
touch(Template(r"tpl1546074092173.png", record_pos=(-0.339, -0.237), resolution=(1366, 768)))
sleep(1)

touch(Template(r"tpl1546934613612.png", record_pos=(-0.444, -0.143), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546520822277.png", record_pos=(0.122, 0.01), resolution=(1366, 768)))
touch(Template(r"tpl1546591423210.png", record_pos=(0.152, -0.088), resolution=(1366, 768)))

touch(Template(r"tpl1546520930485.png", record_pos=(0.295, -0.106), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1546499359252.png", record_pos=(-0.1, -0.156), resolution=(1366, 768)))
touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))
sleep(2)

# 验证属性是否增加显示
prop=poco("com.yhbc.tablet:id/tv_note").get_text()
assert_equal("+香草",prop,"属性显示=+香草")

touch(Template(r"tpl1546521088095.png", record_pos=(-0.329, 0.107), resolution=(1366, 768)))
touch(Template(r"tpl1546521111524.png", record_pos=(0.294, -0.105), resolution=(1366, 768)))
touch(Template(r"tpl1546589072879.png", record_pos=(0.067, 0.156), resolution=(1366, 768)))

touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))
sleep(2)
prop2=poco("com.yhbc.tablet:id/tv_note").get_text()
assert_equal("+价格-1",prop2,"属性显示=价格-1")
# 验证购物车中订单金额是否正确
total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("11.0",total_price,"验证订单总金额是否=11.0")

# 下单
touch(Template(r"tpl1546521705527.png", record_pos=(0.242, -0.184), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1546521744139.png", record_pos=(0.302, -0.185), resolution=(1366, 768)))
touch(Template(r"tpl1546523904395.png", record_pos=(0.247, 0.219), resolution=(1366, 768)))
sleep(2)
poco("com.yhbc.tablet:id/lv_order").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/rl").child("com.yhbc.tablet:id/ll").child("com.yhbc.tablet:id/rl_reduce").child("com.yhbc.tablet:id/tv_reduce").click()
touch(Template(r"tpl1546528990614.png", record_pos=(-0.217, -0.078), resolution=(1366, 768)))
touch(Template(r"tpl1546529053064.png", record_pos=(-0.098, -0.038), resolution=(1366, 768)))
touch(Template(r"tpl1546529062659.png", record_pos=(-0.101, 0.085), resolution=(1366, 768)))
touch(Template(r"tpl1546529073893.png", record_pos=(0.0, 0.005), resolution=(1366, 768)))
touch(Template(r"tpl1546529092862.png", record_pos=(-0.002, 0.137), resolution=(1366, 768)))
sleep(2)

touch(Template(r"tpl1546529131908.png", record_pos=(0.289, -0.141), resolution=(1366, 768)))
sleep(2)
poco("com.yhbc.tablet:id/pack").click()
touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))
sleep(2)
assert_exists(Template(r"tpl1546521341641.png", record_pos=(0.351, 0.031), resolution=(1366, 768)), "菜单显示打包")
# 验证购物车中订单金额是否正确
total_price2=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("8.5",total_price2,"验证订单总金额是否=8.5")
# 下单
touch(Template(r"tpl1546521705527.png", record_pos=(0.242, -0.184), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1546521744139.png", record_pos=(0.302, -0.185), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1546589873332.png", record_pos=(0.413, 0.217), resolution=(1366, 768)))
sleep(2.0)
# 收银台
poco("com.yhbc.tablet:id/iv_erase").click()
sleep(1.0)
poco(text="抹零小数").click()

# touch(Template(r"tpl1546589944922.png", record_pos=(-0.356, 0.018), resolution=(1366, 768)))
sleep(1.0)
#获取收银台应收金额
yingshou=poco("com.yhbc.tablet:id/tv_realprice").get_text()
assert_equal("8.0",yingshou,"验证收银台应收金额=8.0")
#获取收银台抹零金额
moling=poco("com.yhbc.tablet:id/et_bonus").get_text()
assert_equal("0.5",moling,"验证收银台抹零金额=0.5")
touch(Template(r"tpl1546590391549.png", record_pos=(0.177, -0.165), resolution=(1366, 768)))
touch(Template(r"tpl1546590409925.png", record_pos=(-0.043, 0.121), resolution=(1366, 768)))
touch(Template(r"tpl1546590420205.png", record_pos=(0.387, 0.031), resolution=(1366, 768)))
#获取收银台找零金额
zhaoling=poco("com.yhbc.tablet:id/tv_back_maney").get_text()
assert_equal("42.0",zhaoling,"验证收银台找零金额=42.0")

touch(Template(r"tpl1546590427751.png", record_pos=(0.316, 0.12), resolution=(1366, 768)))

sleep(3.0)

# 查看订单
touch(Template(r"tpl1546072136278.png", record_pos=(0.161, -0.236), resolution=(1366, 768)))

sleep(2.0)
# 验证已结账订单金额是否正确
order_total_price=poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.yhbc.tablet:id/viewpager").child("android.widget.LinearLayout").offspring("com.yhbc.tablet:id/order_listview").offspring("com.yhbc.tablet:id/tv_total_price").get_text()


print("order_total_price="+order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("8.0",order_total_price," 订单详情-验证金额总价是否=8.0")

# 验证已结账订单支付方式
pay_mode=poco("com.yhbc.tablet:id/order_listview").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/ll_item").child("com.yhbc.tablet:id/ll_click_pay_model").child("com.yhbc.tablet:id/tv_pay_model").get_text()
assert_equal("人工现金",pay_mode," 订单详情-验证支付方式=人工现金")

