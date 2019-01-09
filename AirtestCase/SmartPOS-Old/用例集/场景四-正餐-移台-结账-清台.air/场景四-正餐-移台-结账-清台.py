# -*- encoding=utf8 -*-
# 场景：开台-订餐人数2人-下单-现金支付-清台
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
touch(Template(r"tpl1546062477694.png", record_pos=(-0.348, -0.064), resolution=(1366, 768)))
sleep(2.0)
assert_exists(Template(r"tpl1545989483597.png", record_pos=(0.0, -0.17), resolution=(1366, 768)), "验证是否弹出订单人数选择框")

touch(Template(r"tpl1545988828587.png", record_pos=(0.002, -0.063), resolution=(1366, 768)))
touch(Template(r"tpl1545988840243.png", record_pos=(-0.002, 0.098), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546934613612.png", record_pos=(-0.444, -0.143), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546077516867.png", record_pos=(-0.223, 0.011), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1545988897393.png", record_pos=(0.425, 0.221), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1545988912844.png", record_pos=(0.316, 0.121), resolution=(1366, 768)))
sleep(3.0)
touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
sleep(2.0)

touch(Template(r"tpl1546063094189.png", record_pos=(-0.352, -0.067), resolution=(1366, 768)))
# sleep(2.0)
# 验证餐具费是否正确
cjf=poco("com.yhbc.tablet:id/orderDetailsListView").child("com.yhbc.tablet:id/rl_resting_orderitem_popu")[1].child("android.widget.LinearLayout").child("com.yhbc.tablet:id/tv_item_price").get_text()
# print("餐具费="+cjf)
assert_equal("2.0",cjf," 两人餐具费=2元")

# 验证订单金额
total_price=poco("com.yhbc.tablet:id/countTextView").get_text()
assert_equal("共2项，合计22.00元",total_price," 两人餐具费=2元")

touch(Template(r"tpl1545989072507.png", record_pos=(0.43, 0.216), resolution=(1366, 768)))
sleep(1.0)
assert_exists(Template(r"tpl1545989148658.png", record_pos=(0.001, -0.018), resolution=(1366, 768)), "验证是否弹出清台提示框")
touch(Template(r"tpl1545989156526.png", record_pos=(0.063, 0.033), resolution=(1366, 768)))
sleep(1.0)
b6_stat=poco("com.yhbc.tablet:id/gv_menu").child("android.widget.RelativeLayout")[5].child("com.yhbc.tablet:id/rl_item").child("android.widget.LinearLayout").child("com.yhbc.tablet:id/tv_state").get_text()
assert_equal("空闲",b6_stat," 验证B6桌台清台是否成功")


