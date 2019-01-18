# -*- encoding=utf8 -*-
# 到店点餐“炸鸡腿（称重1.5）+香草+1+打包+1”，现金收银，拉肚子，要求商家赔偿，最后决定免单，将改订单进行反结账，继续点餐，“炸鸡腿（修改-称重2）+香草+1+打包+1”、“菠萝啤+蓝莓+1+去冰”，会员支付
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 点餐操作
touch(Template(r"tpl1547630570346.png", record_pos=(-0.471, -0.203), resolution=(1366, 768)))
sleep(1)
# touch(Template(r"tpl1547630742496.png", record_pos=(0.452, -0.206), resolution=(1366, 768)))
sleep(1)

touch(Template(r"tpl1547631915083.png", record_pos=(0.346, -0.255), resolution=(1366, 768)))
touch(Template(r"tpl1547631944787.png", record_pos=(-0.056, -0.15), resolution=(1366, 768)))

touch(Template(r"tpl1547631959855.png", record_pos=(-0.057, 0.024), resolution=(1366, 768)))
touch(Template(r"tpl1547631969287.png", record_pos=(0.017, -0.097), resolution=(1366, 768)))
touch(Template(r"tpl1547631988934.png", record_pos=(0.019, 0.219), resolution=(1366, 768)))


sleep(2)

touch(Template(r"tpl1547630868231.png", record_pos=(-0.14, -0.162), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547780750453.png", record_pos=(-0.056, -0.18), resolution=(1366, 768)))
#属性关闭按钮 
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(2)
# 打包 
touch(Template(r"tpl1547631244440.png", record_pos=(-0.141, -0.029), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547631288153.png", record_pos=(-0.059, -0.207), resolution=(1366, 768)))

sleep(1)
#打包关闭按钮 
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(2)
assert_exists(Template(r"tpl1547631378794.png", record_pos=(-0.311, -0.087), resolution=(1366, 768)), "菜单显示打包")
touch(Template(r"tpl1547780856322.png", record_pos=(-0.331, 0.214), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547780910794.png", record_pos=(0.334, 0.214), resolution=(1366, 768)))
sleep(2.0)
# 进行反结账操作
# 查看订单
touch(Template(r"tpl1547632610096.png", record_pos=(-0.469, 0.109), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547632628855.png", record_pos=(-0.103, -0.206), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547781007237.png", record_pos=(0.447, -0.255), resolution=(1366, 768)))
sleep(2.0)
# 验证已结账订单金额是否正确
order_total_price=poco("com.yhbc.yhz.dinner:id/tv_buy_price").get_text()
print("order_total_price="+order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("3.5",order_total_price," 订单详情-验证金额总价是否=3.5")
# 验证订单状态是否为已结账
order_state=poco("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/rl_common").child("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/lv_order").offspring("com.yhbc.yhz.dinner:id/tv_pay_status").get_text()# 获取订单状态值
print("order_state="+order_state)
assert_equal("已结账",order_state," 订单详情-验证订单状态=已结账")
# 进行反结账
# 第一行订单查看按钮
poco("com.yhbc.yhz.dinner:id/tv_operation").click()
touch(Template(r"tpl1547781154983.png", record_pos=(0.177, 0.156), resolution=(1366, 768)))
sleep(1)
assert_exists(Template(r"tpl1547781214610.png", record_pos=(-0.001, -0.018), resolution=(1366, 768)), "验证弹出确定反结账确定窗口")
touch(Template(r"tpl1547781233855.png", record_pos=(0.045, 0.074), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547781276325.png", record_pos=(0.037, -0.135), resolution=(1366, 768)))

sleep(1)
# 输入退款密码
touch(Template(r"tpl1547783712561.png", record_pos=(-0.428, 0.223), resolution=(1366, 768)))
touch(Template(r"tpl1547783725287.png", record_pos=(-0.229, 0.092), resolution=(1366, 768)))
touch(Template(r"tpl1547783895304.png", record_pos=(-0.001, 0.089), resolution=(1366, 768)))
touch(Template(r"tpl1547783902238.png", record_pos=(0.225, 0.091), resolution=(1366, 768)))
touch(Template(r"tpl1547783907419.png", record_pos=(-0.228, 0.133), resolution=(1366, 768)))
touch(Template(r"tpl1547783913498.png", record_pos=(0.001, 0.134), resolution=(1366, 768)))
touch(Template(r"tpl1547783919408.png", record_pos=(0.225, 0.132), resolution=(1366, 768)))
touch(Template(r"tpl1547783925363.png", record_pos=(-0.228, 0.175), resolution=(1366, 768)))

sleep(1)
touch(Template(r"tpl1547781302399.png", record_pos=(0.045, -0.037), resolution=(1366, 768)))

sleep(10)

touch(Template(r"tpl1547799179040.png", record_pos=(-0.141, -0.114), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547799191497.png", record_pos=(0.083, -0.2), resolution=(1366, 768)))

touch(Template(r"tpl1547799235189.png", record_pos=(0.075, 0.138), resolution=(1366, 768)))
touch(Template(r"tpl1547799249060.png", record_pos=(0.017, 0.217), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547799301830.png", record_pos=(-0.244, 0.212), resolution=(1366, 768)))

sleep(2.0)

touch(Template(r"tpl1547799408882.png", record_pos=(0.335, 0.212), resolution=(1366, 768)))
sleep(5)
# 验证已结账订单金额是否正确
fjz_order_total_price=poco("com.yhbc.yhz.dinner:id/tv_buy_price").get_text()
print("fjz_order_total_price="+fjz_order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("1.0",fjz_order_total_price," 订单详情-验证金额总价")

# 验证已结账订单支付方式
fjz_pay_mode=poco("com.yhbc.yhz.dinner:id/lv_order").child("com.yhbc.yhz.dinner:id/layout_item")[0].child("com.yhbc.yhz.dinner:id/tv_pay_mode").get_text()
assert_equal("混合支付",fjz_pay_mode," 订单详情-验证支付方式")

# 验证订单状态是否为已退款
fjz_order_state=poco("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/rl_common").child("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/lv_order").offspring("com.yhbc.yhz.dinner:id/tv_pay_status").get_text()# 获取订单状态值
print("fjz_order_state="+fjz_order_state)
assert_equal("已结账",fjz_order_state," 订单详情-验证反结账之后订单状态")

# 还原桌面
touch(Template(r"tpl1547783142856.png", record_pos=(-0.454, -0.254), resolution=(1366, 768)))



