# -*- encoding=utf8 -*-
# 场景一：顾客到店，点选“焦糖奶茶-中杯+1元香草”、“波霸奶茶+去冰”、“菠萝啤+打包+打包费1元”。下单后，退掉波霸奶茶，改为“炸鸡腿（称重）+不加辣”，用餐完毕，会员卡结账，享受8折优惠。结账核对账单，

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

touch(Template(r"tpl1546520822277.png", record_pos=(0.122, 0.01), resolution=(1366, 768)))
touch(Template(r"tpl1546520834322.png", record_pos=(0.156, -0.084), resolution=(1366, 768)))
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
touch(Template(r"tpl1546499369153.png", record_pos=(-0.018, -0.158), resolution=(1366, 768)))
touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))
sleep(2)
prop2=poco("com.yhbc.tablet:id/tv_note").get_text()
assert_equal("+去冰",prop2,"属性显示=+去冰")

touch(Template(r"tpl1546521220047.png", record_pos=(-0.328, 0.012), resolution=(1366, 768)))
touch(Template(r"tpl1546521240997.png", record_pos=(0.3, -0.105), resolution=(1366, 768)))
poco("com.yhbc.tablet:id/pack").click()
touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))
sleep(2)

# prop3=poco("com.yhbc.tablet:id/tv_note").get_text()
# print("prop3="+prop3)
# # assert_equal("【打包】",prop3,"属性显示=【打包】")
assert_exists(Template(r"tpl1546523530256.png", record_pos=(0.351, -0.102), resolution=(1366, 768)), "菠萝啤增加成功")

assert_exists(Template(r"tpl1546521341641.png", record_pos=(0.351, 0.031), resolution=(1366, 768)), "菜单显示打包")
# 验证购物车中订单金额是否正确
total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("18.0",total_price,"验证订单总金额是否=18.0")

# 下单
touch(Template(r"tpl1546521705527.png", record_pos=(0.242, -0.184), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1546521744139.png", record_pos=(0.302, -0.185), resolution=(1366, 768)))
touch(Template(r"tpl1546523904395.png", record_pos=(0.247, 0.219), resolution=(1366, 768)))
sleep(2)
poco("com.yhbc.tablet:id/lv_order").child("android.widget.LinearLayout")[1].child("com.yhbc.tablet:id/rl").child("com.yhbc.tablet:id/ll").child("com.yhbc.tablet:id/rl_reduce").child("com.yhbc.tablet:id/tv_reduce").click()

#输入退菜密码
# poco("com.yhbc.tablet:id/btn_goodType").click()
# poco(text="等待时间过长").click()
# poco("com.yhbc.tablet:id/popu_password").click()
# text("123456")
# poco("com.yhbc.tablet:id/btn_admit").click()
# poco("com.yhbc.tablet:id/iv_close").click()
touch(Template(r"tpl1546528990614.png", record_pos=(-0.217, -0.078), resolution=(1366, 768)))
touch(Template(r"tpl1546529053064.png", record_pos=(-0.098, -0.038), resolution=(1366, 768)))
touch(Template(r"tpl1546529062659.png", record_pos=(-0.101, 0.085), resolution=(1366, 768)))
touch(Template(r"tpl1546529073893.png", record_pos=(0.0, 0.005), resolution=(1366, 768)))
touch(Template(r"tpl1546529092862.png", record_pos=(-0.002, 0.137), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1546529131908.png", record_pos=(0.289, -0.141), resolution=(1366, 768)))
touch(Template(r"tpl1546529154482.png", record_pos=(0.152, -0.068), resolution=(1366, 768)))
touch(Template(r"tpl1546529163691.png", record_pos=(-0.239, 0.199), resolution=(1366, 768)))
# 验证属性是否增加显示
prop4=poco("com.yhbc.tablet:id/tv_note").get_text()
assert_equal("+不加辣",prop4,"属性显示=+不加辣")

# 验证购物车中订单金额是否正确
total_price2=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("13.5",total_price2,"验证订单总金额是否=13.5")

touch(Template(r"tpl1546521705527.png", record_pos=(0.242, -0.184), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1546530896621.png", record_pos=(0.302, -0.185), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1546530922563.png", record_pos=(0.417, 0.218), resolution=(1366, 768)))

# 会员支付
touch(Template(r"tpl1546509584198.png", record_pos=(-0.228, 0.094), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1546510056823.png", record_pos=(-0.041, -0.025), resolution=(1366, 768)))
touch(Template(r"tpl1546510063726.png", record_pos=(0.102, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510100461.png", record_pos=(0.102, 0.056), resolution=(1366, 768)))
touch(Template(r"tpl1546510092623.png", record_pos=(0.244, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546529628944.png", record_pos=(0.243, 0.055), resolution=(1366, 768)))
touch(Template(r"tpl1546510056823.png", record_pos=(-0.041, -0.025), resolution=(1366, 768)))
touch(Template(r"tpl1546510092623.png", record_pos=(0.244, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510063726.png", record_pos=(0.102, 0.018), resolution=(1366, 768)))
touch(Template(r"tpl1546510056823.png", record_pos=(-0.041, -0.025), resolution=(1366, 768)))
touch(Template(r"tpl1546529704663.png", record_pos=(-0.044, 0.02), resolution=(1366, 768)))
touch(Template(r"tpl1546529628944.png", record_pos=(0.243, 0.055), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546509662836.png", record_pos=(0.424, -0.118), resolution=(1366, 768)))
sleep(2)
# 验证会员查询是否成功
member_no=poco("com.yhbc.tablet:id/tv_usert").get_text()
assert_equal("15869165149",member_no,"收银台会员支付，查询会员，账号")
touch(Template(r"tpl1546509675618.png", record_pos=(0.316, 0.135), resolution=(1366, 768)))
sleep(3.0)

# 查看订单
touch(Template(r"tpl1546072136278.png", record_pos=(0.161, -0.236), resolution=(1366, 768)))

sleep(2.0)
# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.tablet:id/tv_total_price").get_text()
print("order_total_price="+order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("11.8",order_total_price," 订单详情-验证金额总价是否=11.8")

# 验证已结账订单支付方式
pay_mode=poco("com.yhbc.tablet:id/order_listview").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/ll_item").child("com.yhbc.tablet:id/ll_click_pay_model").child("com.yhbc.tablet:id/tv_pay_model").get_text()
assert_equal("会员卡",pay_mode," 订单详情-验证支付方式=会员卡")

