# -*- encoding=utf8 -*-
__author__ = "lsd"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
touch(Template(r"tpl1546074092173.png", record_pos=(-0.339, -0.237), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546509518945.png", record_pos=(-0.105, -0.176), resolution=(1366, 768)))

touch(Template(r"tpl1546509549500.png", record_pos=(0.422, 0.222), resolution=(1366, 768)))

sleep(2.0)
touch(Template(r"tpl1546509584198.png", record_pos=(-0.228, 0.094), resolution=(1366, 768)))
touch(Template(r"tpl1546510056823.png", record_pos=(-0.041, -0.025), resolution=(1366, 768)))
touch(Template(r"tpl1546510063726.png", record_pos=(0.102, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510063726.png", record_pos=(0.102, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510063726.png", record_pos=(0.102, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510076431.png", record_pos=(-0.045, 0.055), resolution=(1366, 768)))
touch(Template(r"tpl1546510056823.png", record_pos=(-0.041, -0.025), resolution=(1366, 768)))
touch(Template(r"tpl1546510092623.png", record_pos=(0.244, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510100461.png", record_pos=(0.102, 0.056), resolution=(1366, 768)))
touch(Template(r"tpl1546510092623.png", record_pos=(0.244, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510092623.png", record_pos=(0.244, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510113059.png", record_pos=(0.242, -0.02), resolution=(1366, 768)))
touch(Template(r"tpl1546509662836.png", record_pos=(0.424, -0.118), resolution=(1366, 768)))
sleep(2)
# 验证会员查询是否成功
member_no=poco("com.yhbc.tablet:id/tv_usert").get_text()
assert_equal("15557168663",member_no,"收银台会员支付，查询会员，账号")
touch(Template(r"tpl1546509675618.png", record_pos=(0.316, 0.135), resolution=(1366, 768)))
sleep(2.0)

snapshot(msg="下单成功截图")
touch(Template(r"tpl1546072136278.png", record_pos=(0.161, -0.236), resolution=(1366, 768)))

sleep(2.0)
# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.tablet:id/tv_total_price").get_text()
print("order_total_price="+order_total_price)
assert_equal("0.01",order_total_price," 订单详情-验证金额总价是否=0.01")

# 验证已结账订单支付方式
pay_mode=poco("com.yhbc.tablet:id/order_listview").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/ll_item").child("com.yhbc.tablet:id/ll_click_pay_model").child("com.yhbc.tablet:id/tv_pay_model").get_text()
assert_equal("会员卡",pay_mode," 订单详情-验证支付方式=会员卡")



