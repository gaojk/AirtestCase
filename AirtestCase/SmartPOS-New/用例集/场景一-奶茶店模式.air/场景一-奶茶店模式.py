# -*- encoding=utf8 -*-
# 场景一：顾客到店，点选“焦糖奶茶-中杯+1元香草”、“波霸奶茶+去冰”、“菠萝啤+打包+打包费1元”。下单后，退掉波霸奶茶，改为“炸鸡腿（称重）+不加辣”，用餐完毕，会员卡结账，享受8折优惠。结账核对账单，

__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
stop_app("com.yhbc.yhz.dinner")
start_app("com.yhbc.yhz.dinner",activity=None)
sleep(3)
touch(Template(r"tpl1551372987427.png", record_pos=(-0.001, -0.013), resolution=(1366, 768)))
sleep(8)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
# 点餐操作
touch(Template(r"tpl1547630570346.png", record_pos=(-0.471, -0.203), resolution=(1366, 768)))

sleep(1)
touch(Template(r"tpl1547630742496.png", record_pos=(0.452, -0.206), resolution=(1366, 768)))

sleep(1)
touch(Template(r"tpl1547630782370.png", record_pos=(0.047, -0.173), resolution=(1366, 768)))

touch(Template(r"tpl1547630811299.png", record_pos=(0.053, -0.055), resolution=(1366, 768)))

sleep(2)
touch(Template(r"tpl1547630868231.png", record_pos=(-0.14, -0.162), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547630884528.png", record_pos=(-0.056, -0.113), resolution=(1366, 768)))
sleep(1)
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(2)

# 验证属性是否增加显示
prop=poco("com.yhbc.yhz.dinner:id/tv_property").get_text()

assert_equal("+香草",prop,"属性显示=+香草")
touch(Template(r"tpl1547631039247.png", record_pos=(0.158, -0.17), resolution=(1366, 768)))

sleep(1)
touch(Template(r"tpl1547630868231.png", record_pos=(-0.14, -0.162), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547631090534.png", record_pos=(0.1, -0.179), resolution=(1366, 768)))
sleep(1)
poco("com.yhbc.yhz.dinner:id/iv_close").click()

sleep(2)
prop2=poco("com.yhbc.yhz.dinner:id/tv_property").get_text()
assert_equal("+去冰",prop2,"属性显示=+去冰")
touch(Template(r"tpl1547631219226.png", record_pos=(0.044, -0.253), resolution=(1366, 768)))

# 打包 
touch(Template(r"tpl1547631244440.png", record_pos=(-0.141, -0.029), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547631288153.png", record_pos=(-0.059, -0.207), resolution=(1366, 768)))
#关闭按钮 
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(2)
assert_exists(Template(r"tpl1547631378794.png", record_pos=(-0.311, -0.087), resolution=(1366, 768)), "菜单显示打包")

# 下单
touch(Template(r"tpl1547631550762.png", record_pos=(-0.415, -0.26), resolution=(1366, 768)))

sleep(1.0)
touch(Template(r"tpl1547631577912.png", record_pos=(-0.364, -0.258), resolution=(1366, 768)))
sleep(2.0)
# 验证购物车中订单金额是否正确
# total_price=poco("com.yhbc.yhz.dinner:id/tv_total").get_text()
# assert_equal("共4份，合计￥18",total_price,"验证订单总金额=18")

touch(Template(r"tpl1547631607260.png", record_pos=(0.212, 0.134), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1547631835393.png", record_pos=(-0.34, -0.174), resolution=(1366, 768)))
touch(Template(r"tpl1547631856692.png", record_pos=(-0.141, 0.086), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547631881265.png", record_pos=(0.09, 0.213), resolution=(1366, 768)))
sleep(1)

#输入退菜密码
# poco("com.yhbc.tablet:id/btn_goodType").click()
# poco(text="等待时间过长").click()
# poco("com.yhbc.tablet:id/popu_password").click()
# text("123456")
# poco("com.yhbc.tablet:id/btn_admit").click()
# poco("com.yhbc.tablet:id/iv_close").click()
touch(Template(r"tpl1547631915083.png", record_pos=(0.346, -0.255), resolution=(1366, 768)))
touch(Template(r"tpl1547631944787.png", record_pos=(-0.056, -0.15), resolution=(1366, 768)))

touch(Template(r"tpl1547631959855.png", record_pos=(-0.057, 0.024), resolution=(1366, 768)))
touch(Template(r"tpl1547631969287.png", record_pos=(0.017, -0.097), resolution=(1366, 768)))
touch(Template(r"tpl1547631988934.png", record_pos=(0.019, 0.219), resolution=(1366, 768)))

sleep(2)
touch(Template(r"tpl1547630868231.png", record_pos=(-0.14, -0.162), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547632056210.png", record_pos=(0.174, -0.032), resolution=(1366, 768)))
sleep(1)
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(2)
prop3=poco("com.yhbc.yhz.dinner:id/tv_property").get_text()
assert_equal("+不加辣",prop3,"属性显示=+不加辣")

# 验证购物车中订单金额是否正确
total_price2=poco("com.yhbc.yhz.dinner:id/tv_order_total").get_text()
assert_equal("共 4 份，合计 13.5 元",total_price2,"验证订单总金额是否=13.5")

touch(Template(r"tpl1547631550762.png", record_pos=(-0.415, -0.26), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547631577912.png", record_pos=(-0.364, -0.258), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547631607260.png", record_pos=(0.212, 0.134), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1547632311143.png", record_pos=(-0.242, 0.212), resolution=(1366, 768)))
sleep(1)

# 会员支付
touch(Template(r"tpl1547632344050.png", record_pos=(0.143, 0.013), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1547632368213.png", record_pos=(0.231, -0.065), resolution=(1366, 768)))
touch(Template(r"tpl1547632374545.png", record_pos=(0.299, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1547632415104.png", record_pos=(0.298, 0.046), resolution=(1366, 768)))
touch(Template(r"tpl1547632400744.png", record_pos=(0.367, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1547633369607.png", record_pos=(0.368, 0.047), resolution=(1366, 768)))
touch(Template(r"tpl1547632368213.png", record_pos=(0.231, -0.065), resolution=(1366, 768)))
touch(Template(r"tpl1547632400744.png", record_pos=(0.367, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1547632374545.png", record_pos=(0.299, -0.011), resolution=(1366, 768)))
touch(Template(r"tpl1547632368213.png", record_pos=(0.231, -0.065), resolution=(1366, 768)))
touch(Template(r"tpl1547633419423.png", record_pos=(0.231, -0.012), resolution=(1366, 768)))
touch(Template(r"tpl1547633425332.png", record_pos=(0.366, 0.046), resolution=(1366, 768)))

sleep(1)
touch(Template(r"tpl1547632454911.png", record_pos=(0.26, 0.215), resolution=(1366, 768)))

sleep(2)
# 验证会员查询是否成功
member_no=poco("com.yhbc.yhz.dinner:id/tv_user").get_text()
assert_equal("账号: 15869165149",member_no,"收银台会员支付，查询会员，账号")

touch(Template(r"tpl1547632556603.png", record_pos=(0.045, 0.071), resolution=(1366, 768)))
touch(Template(r"tpl1547632578154.png", record_pos=(0.405, 0.214), resolution=(1366, 768)))

sleep(3.0)

# 查看订单
touch(Template(r"tpl1547632610096.png", record_pos=(-0.469, 0.109), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547632628855.png", record_pos=(-0.103, -0.206), resolution=(1366, 768)))
sleep(2.0)
# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.yhz.dinner:id/tv_buy_price").get_text()

print("order_total_price="+order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("10.8",order_total_price," 订单详情-验证金额总价是否=10.8")

# 验证已结账订单支付方式
pay_mode=poco("com.yhbc.yhz.dinner:id/lv_order").child("com.yhbc.yhz.dinner:id/layout_item")[0].child("com.yhbc.yhz.dinner:id/tv_pay_mode").get_text()
assert_equal("会员卡",pay_mode," 订单详情-验证支付方式=会员卡")

touch(Template(r"tpl1547783142856.png", record_pos=(-0.454, -0.254), resolution=(1366, 768)))



