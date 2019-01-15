# -*- encoding=utf8 -*-
# 到店点餐“炸鸡腿（称重1.5）+香草+1+打包+1”，现金收银，拉肚子，要求商家赔偿，最后决定免单，将改订单进行反结账，继续点餐，“炸鸡腿（修改-称重2）+香草+1+打包+1”、“菠萝啤+蓝莓+1+去冰”，会员支付
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

touch(Template(r"tpl1546528990614.png", record_pos=(-0.217, -0.078), resolution=(1366, 768)))
touch(Template(r"tpl1546529053064.png", record_pos=(-0.098, -0.038), resolution=(1366, 768)))
touch(Template(r"tpl1546529062659.png", record_pos=(-0.101, 0.085), resolution=(1366, 768)))
touch(Template(r"tpl1546529073893.png", record_pos=(0.0, 0.005), resolution=(1366, 768)))
touch(Template(r"tpl1546529092862.png", record_pos=(-0.002, 0.137), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1546529131908.png", record_pos=(0.289, -0.141), resolution=(1366, 768)))
sleep(2)
poco("com.yhbc.tablet:id/pack").click()#点击打包
sleep(1)
touch(Template(r"tpl1546499359252.png", record_pos=(-0.1, -0.156), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))
sleep(2)
assert_exists(Template(r"tpl1546521341641.png", record_pos=(0.351, 0.031), resolution=(1366, 768)), "菜单显示打包")
# 验证购物车中订单金额是否正确
total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("3.5",total_price,"验证商品+打包费金额是否=3.5")

touch(Template(r"tpl1546071932023.png", record_pos=(0.283, 0.222), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546071972568.png", record_pos=(0.313, 0.121), resolution=(1366, 768)))
sleep(2.0)
# 进行反结账操作
# 查看订单
touch(Template(r"tpl1546072136278.png", record_pos=(0.161, -0.236), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546841008291.png", record_pos=(0.454, -0.179), resolution=(1366, 768)))

sleep(2.0)
# 获取订单号
order_num=poco("com.yhbc.tablet:id/tv_order_num").get_text()
print("order_num="+order_num)

# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.tablet:id/tv_total_price").get_text()
print("order_total_price="+order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("3.5",order_total_price," 订单详情-验证金额总价是否=3.5")
poco("com.yhbc.tablet:id/tv_operation").click() # 第一单“查看”按钮
# 进行反结账
touch(Template(r"tpl1546840777425.png", record_pos=(0.21, 0.168), resolution=(1366, 768)))
sleep(1)
assert_exists(Template(r"tpl1546829336497.png", record_pos=(0.0, -0.008), resolution=(1366, 768)), "验证弹出确定反结账确定窗口")
touch(Template(r"tpl1546829581356.png", record_pos=(0.064, 0.098), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546829650637.png", record_pos=(0.037, -0.146), resolution=(1366, 768)))

touch(Template(r"tpl1546829687208.png", record_pos=(-0.018, -0.12), resolution=(1366, 768)))

touch(Template(r"tpl1546829736991.png", record_pos=(0.036, -0.1), resolution=(1366, 768)))
sleep(1)
# keyevent("1234567")
text("1234567")

sleep(1)
touch(Template(r"tpl1546829828640.png", record_pos=(0.043, -0.037), resolution=(1366, 768)))
assert_exists(Template(r"tpl1546842232120.png", record_pos=(0.002, -0.007), resolution=(1366, 768)), "弹出反结账弹出框")

touch(Template(r"tpl1546845358074.png", record_pos=(0.065, 0.098), resolution=(1366, 768)))
sleep(1)
assert_exists(Template(r"tpl1546845410245.png", record_pos=(-0.324, -0.234), resolution=(1366, 768)), "验证是否进入反结账页面")

touch(Template(r"tpl1546845533405.png", record_pos=(0.394, -0.142), resolution=(1366, 768)))
touch(Template(r"tpl1546845557810.png", record_pos=(0.097, 0.088), resolution=(1366, 768)))
touch(Template(r"tpl1546845557810.png", record_pos=(0.097, 0.088), resolution=(1366, 768)))
touch(Template(r"tpl1546845557810.png", record_pos=(0.097, 0.088), resolution=(1366, 768)))
touch(Template(r"tpl1546845623686.png", record_pos=(0.0, -0.037), resolution=(1366, 768)))
touch(Template(r"tpl1546845638761.png", record_pos=(0.078, 0.135), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1546521220047.png", record_pos=(-0.328, 0.012), resolution=(1366, 768)))
touch(Template(r"tpl1546521240997.png", record_pos=(0.3, -0.105), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1546845908171.png", record_pos=(-0.019, -0.155), resolution=(1366, 768)))

touch(Template(r"tpl1546845946184.png", record_pos=(0.067, -0.154), resolution=(1366, 768)))
touch(Template(r"tpl1546845957574.png", record_pos=(-0.238, 0.198), resolution=(1366, 768)))
# 验证属性是否增加显示
prop=poco("com.yhbc.tablet:id/tv_note").get_text()
assert_equal("+蓝莓+去冰",prop,"属性显示=+蓝莓+去冰")

# 验证购物车中订单金额是否正确
fjz_total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("10.0",fjz_total_price,"验证订单总金额是否=10.0")
touch(Template(r"tpl1546846212256.png", record_pos=(0.444, 0.225), resolution=(1366, 768)))

sleep(2.0)
touch(Template(r"tpl1546509584198.png", record_pos=(-0.228, 0.094), resolution=(1366, 768)))
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
touch(Template(r"tpl1546509675618.png", record_pos=(0.316, 0.135), resolution=(1366, 768)))
sleep(3.0)

snapshot(msg="下单成功截图")
touch(Template(r"tpl1546072136278.png", record_pos=(0.161, -0.236), resolution=(1366, 768)))

sleep(2.0)
# 获取反结账订单号
fjz_order_num=poco("com.yhbc.tablet:id/tv_order_num").get_text()
print("fjz_order_num="+fjz_order_num)
assert_equal(order_num,fjz_order_num," 原订单号=反结账订单订单号")

# 验证已结账订单金额是否正确
fjz_order_total_price=poco("com.yhbc.tablet:id/tv_total_price").get_text()
print("order_total_price="+fjz_order_total_price)
assert_equal("10.0",fjz_order_total_price," 反结账订单详情-验证金额总价是否=10")

# 验证已结账订单支付方式
fjz_pay_mode=poco("com.yhbc.tablet:id/order_listview").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/ll_item").child("com.yhbc.tablet:id/ll_click_pay_model").child("com.yhbc.tablet:id/tv_pay_model").get_text()
assert_equal("会员卡",fjz_pay_mode," 订单详情-验证支付方式=会员卡")

# 验证订单状态是否为已退款
fjz_order_state=poco("com.yhbc.tablet:id/order_listview").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/ll_item").child("com.yhbc.tablet:id/tv_pay_status").get_text()# 获取订单状态值
print("fjz_order_state="+fjz_order_state)
assert_equal("已结账",fjz_order_state," 订单详情-验证订单状态=已结账")



