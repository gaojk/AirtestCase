# -*- encoding=utf8 -*-
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
# stop_app("com.yhbc.yhz.dinner")

# #  start_app_timing("com.yhbc.yhz.dinner","com.yhbc.tablet.ui.main.MainActivity")
# start_app("com.yhbc.yhz.dinner",activity=None)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 点餐操作
touch(Template(r"tpl1547630570346.png", record_pos=(-0.471, -0.203), resolution=(1366, 768)))
sleep(1)
# touch(Template(r"tpl1547630742496.png", record_pos=(0.452, -0.206), resolution=(1366, 768)))
sleep(1)

touch(Template(r"tpl1547631039247.png", record_pos=(0.158, -0.17), resolution=(1366, 768)))

sleep(1)
# 打包 
touch(Template(r"tpl1547631244440.png", record_pos=(-0.141, -0.029), resolution=(1366, 768)))
sleep(3)
touch(Template(r"tpl1547631288153.png", record_pos=(-0.059, -0.207), resolution=(1366, 768)))

sleep(1)
#打包关闭按钮 
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(2)
assert_exists(Template(r"tpl1547631378794.png", record_pos=(-0.311, -0.087), resolution=(1366, 768)), "菜单显示打包")

touch(Template(r"tpl1547631219226.png", record_pos=(0.044, -0.253), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547630868231.png", record_pos=(-0.14, -0.162), resolution=(1366, 768)))
touch(Template(r"tpl1548043300728.png", record_pos=(0.02, -0.18), resolution=(1366, 768)))
touch(Template(r"tpl1548043315822.png", record_pos=(0.099, -0.182), resolution=(1366, 768)))
#属性关闭按钮 
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(2)

# 验证属性是否增加显示
prop=poco("com.yhbc.yhz.dinner:id/tv_property").get_text()
assert_equal("+蓝莓+去冰",prop,"属性显示=+蓝莓+去冰")

touch(Template(r"tpl1547780856322.png", record_pos=(-0.331, 0.214), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1548043518507.png", record_pos=(0.403, 0.155), resolution=(1366, 768)))
touch(Template(r"tpl1548043528582.png", record_pos=(0.435, -0.065), resolution=(1366, 768)))
touch(Template(r"tpl1548054202672.png", record_pos=(0.335, 0.214), resolution=(1366, 768)))

sleep(5)
touch(Template(r"tpl1548053320624.png", record_pos=(-0.039, 0.08), resolution=(1366, 768)))
sleep(3.0)
touch(Template(r"tpl1548052996562.png", record_pos=(0.365, -0.187), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1548052816834.png", record_pos=(0.401, 0.155), resolution=(1366, 768)))
sleep(5)
touch(Template(r"tpl1548052827431.png", record_pos=(0.231, -0.067), resolution=(1366, 768)))
sleep(6)
touch(Template(r"tpl1548146566590.png", record_pos=(0.333, 0.209), resolution=(1366, 768)))
sleep(6)

# 会员支付

touch(Template(r"tpl1547632344050.png", record_pos=(0.143, 0.013), resolution=(1366, 768)))

# touch(Template(r"tpl1548053011292.png", record_pos=(0.368, -0.146), resolution=(1366, 768)))
sleep(3)
touch(Template(r"tpl1547632368213.png", record_pos=(0.231, -0.065), resolution=(1366, 768)))

touch(Template(r"tpl1547632374545.png", record_pos=(0.299, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1547632374545.png", record_pos=(0.299, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1547632374545.png", record_pos=(0.299, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1548043609859.png", record_pos=(0.233, 0.046), resolution=(1366, 768)))
touch(Template(r"tpl1547632368213.png", record_pos=(0.231, -0.065), resolution=(1366, 768)))
touch(Template(r"tpl1547632400744.png", record_pos=(0.367, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1548043632453.png", record_pos=(0.301, 0.046), resolution=(1366, 768)))
touch(Template(r"tpl1547632400744.png", record_pos=(0.367, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1547632400744.png", record_pos=(0.367, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1548043653119.png", record_pos=(0.367, -0.066), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547632454911.png", record_pos=(0.26, 0.215), resolution=(1366, 768)))

sleep(2)
# 验证会员查询是否成功
member_no=poco("com.yhbc.yhz.dinner:id/tv_user").get_text()
assert_equal("账号: 15557168663",member_no,"收银台会员支付，查询会员，账号")
touch(Template(r"tpl1547632556603.png", record_pos=(0.045, 0.071), resolution=(1366, 768)))

touch(Template(r"tpl1548043826259.png", record_pos=(0.406, 0.212), resolution=(1366, 768)))




sleep(2.0)
# 查看订单
touch(Template(r"tpl1547632610096.png", record_pos=(-0.469, 0.109), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547632628855.png", record_pos=(-0.103, -0.206), resolution=(1366, 768)))
sleep(5.0)
# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.yhz.dinner:id/tv_buy_price").get_text()
print("order_total_price="+order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("13.0",order_total_price," 订单详情-验证金额总价是否=11.8")

# 验证已结账订单支付方式
pay_mode=poco("com.yhbc.yhz.dinner:id/lv_order").child("com.yhbc.yhz.dinner:id/layout_item")[0].child("com.yhbc.yhz.dinner:id/tv_pay_mode").get_text()
assert_equal("混合支付",pay_mode," 订单详情-验证支付方式=会员卡")
# 验证订单状态
order_state=poco("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/rl_common").child("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/lv_order").offspring("com.yhbc.yhz.dinner:id/tv_pay_status").get_text()# 获取订单状态值
print("order_state="+order_state)
assert_equal("已结账",order_state," 订单详情-验证反结账之后订单状态")
# 还原桌面
touch(Template(r"tpl1547783142856.png", record_pos=(-0.454, -0.254), resolution=(1366, 768)))





