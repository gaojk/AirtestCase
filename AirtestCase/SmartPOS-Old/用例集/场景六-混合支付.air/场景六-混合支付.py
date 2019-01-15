# -*- encoding=utf8 -*-
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
# 点餐操作
touch(Template(r"tpl1546074092173.png", record_pos=(-0.339, -0.237), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546934613612.png", record_pos=(-0.444, -0.143), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546521088095.png", record_pos=(-0.329, 0.107), resolution=(1366, 768)))
touch(Template(r"tpl1546521111524.png", record_pos=(0.294, -0.105), resolution=(1366, 768)))
sleep(1)
# 打包 
poco("com.yhbc.tablet:id/pack").click()
touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))
sleep(2)
assert_exists(Template(r"tpl1546521341641.png", record_pos=(0.351, 0.031), resolution=(1366, 768)), "菜单显示打包")

touch(Template(r"tpl1546521220047.png", record_pos=(-0.328, 0.012), resolution=(1366, 768)))
touch(Template(r"tpl1546521240997.png", record_pos=(0.3, -0.105), resolution=(1366, 768)))
sleep(1)

touch(Template(r"tpl1546845908171.png", record_pos=(-0.019, -0.155), resolution=(1366, 768)))

touch(Template(r"tpl1546845946184.png", record_pos=(0.067, -0.154), resolution=(1366, 768)))
touch(Template(r"tpl1546845957574.png", record_pos=(-0.238, 0.198), resolution=(1366, 768)))
sleep(2)

# 验证属性是否增加显示
prop=poco("com.yhbc.tablet:id/tv_note").get_text()
assert_equal("+蓝莓+去冰",prop,"属性显示=+蓝莓+去冰")

# 验证购物车中订单金额是否正确
total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("13.0",total_price,"验证订单总金额是否=13.0")
touch(Template(r"tpl1546071932023.png", record_pos=(0.283, 0.222), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547006278365.png", record_pos=(0.1, 0.12), resolution=(1366, 768)))
touch(Template(r"tpl1547006330570.png", record_pos=(0.387, -0.056), resolution=(1366, 768)))
touch(Template(r"tpl1547006345334.png", record_pos=(0.317, 0.123), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1546509584198.png", record_pos=(-0.228, 0.094), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1547006579084.png", record_pos=(0.22, -0.171), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547006421677.png", record_pos=(-0.044, 0.121), resolution=(1366, 768)))
touch(Template(r"tpl1547006445682.png", record_pos=(-0.045, -0.055), resolution=(1366, 768)))

sleep(1)
# 点击会员卡账号输入框 
poco("com.yhbc.tablet:id/et_print").click()

sleep(2)
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
touch(Template(r"tpl1547522417756.png", record_pos=(0.245, -0.017), resolution=(1366, 768)))

touch(Template(r"tpl1546509662836.png", record_pos=(0.424, -0.118), resolution=(1366, 768)))
sleep(3)
# 验证会员查询是否成功
member_no=poco("com.yhbc.tablet:id/tv_usert").get_text()
assert_equal("15557168663",member_no,"收银台会员支付，查询会员，账号")

# 继续支持按钮 
poco("com.yhbc.tablet:id/btn_pay_Confirm").click()
# touch(Template(r"tpl1547006505729.png", record_pos=(0.316, 0.124), resolution=(1366, 768)))

sleep(3.0)
touch(Template(r"tpl1547006787270.png", record_pos=(-0.432, 0.167), resolution=(1366, 768)))
touch(Template(r"tpl1547006505729.png", record_pos=(0.316, 0.124), resolution=(1366, 768)))

sleep(2.0)
# 查看订单
touch(Template(r"tpl1546072136278.png", record_pos=(0.161, -0.236), resolution=(1366, 768)))

sleep(2.0)
# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.tablet:id/tv_total_price").get_text()
print("order_total_price="+order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("13.0",order_total_price," 订单详情-验证金额总价是否=13")

# 验证已结账订单支付方式
pay_mode=poco("com.yhbc.tablet:id/order_listview").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/ll_item").child("com.yhbc.tablet:id/ll_click_pay_model").child("com.yhbc.tablet:id/tv_pay_model").get_text()
assert_equal("混合支付",pay_mode," 订单详情-验证支付方式=混合支付")

# 验证订单状态是否为已结帐
order_state=poco("com.yhbc.tablet:id/order_listview").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/ll_item").child("com.yhbc.tablet:id/tv_pay_status").get_text()# 获取订单状态值
print("order_state="+order_state)
assert_equal("已结账",order_state," 订单详情-验证订单状态=已结账")


#  点击订单详情 
poco("com.yhbc.tablet:id/order_listview").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/ll_item").child("com.yhbc.tablet:id/ll_click_pay_model").child("com.yhbc.tablet:id/im_mixpay_icon").click()
sleep(1.0)

# 验证混合支付订单 
exists(Template(r"tpl1547012838415.png", record_pos=(-0.001, -0.006), resolution=(1366, 768)))
# 点击混合支付框，关闭按钮 
poco("android.widget.ImageView").click()


