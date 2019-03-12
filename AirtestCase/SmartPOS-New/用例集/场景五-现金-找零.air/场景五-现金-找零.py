# -*- encoding=utf8 -*-
# 场景五：到店点餐点“焦糖奶茶-中杯+1元香草”，“波霸奶茶+价格-1”、下单，退一个“焦糖奶茶-中杯+1元香草”，改为“炸鸡腿（称重）+打包”，菜品上齐结账，和商家协商抹零操作，现金-找零，结账后查看宝报表
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
stop_app("com.yhbc.yhz.dinner")
start_app("com.yhbc.yhz.dinner",activity=None)
sleep(5)
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

touch(Template(r"tpl1547631039247.png", record_pos=(0.158, -0.17), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547630868231.png", record_pos=(-0.14, -0.162), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1548055122381.png", record_pos=(0.059, 0.128), resolution=(1366, 768)))
sleep(1)
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(1)
touch(Template(r"tpl1548055225423.png", record_pos=(-0.417, -0.259), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1548055278305.png", record_pos=(-0.366, -0.258), resolution=(1366, 768)))
touch(Template(r"tpl1548055294391.png", record_pos=(0.211, 0.135), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1548055601616.png", record_pos=(-0.346, -0.171), resolution=(1366, 768)))
touch(Template(r"tpl1548055628490.png", record_pos=(-0.139, 0.087), resolution=(1366, 768)))
touch(Template(r"tpl1548055643326.png", record_pos=(0.091, 0.214), resolution=(1366, 768)))

sleep(2.0)
touch(Template(r"tpl1547631915083.png", record_pos=(0.346, -0.255), resolution=(1366, 768)))
touch(Template(r"tpl1547631944787.png", record_pos=(-0.056, -0.15), resolution=(1366, 768)))

touch(Template(r"tpl1552361690780.png", record_pos=(-0.054, 0.012), resolution=(1366, 768)))

touch(Template(r"tpl1547631969287.png", record_pos=(0.017, -0.097), resolution=(1366, 768)))
touch(Template(r"tpl1547631988934.png", record_pos=(0.019, 0.219), resolution=(1366, 768)))
sleep(1)
# 打包 
touch(Template(r"tpl1547631244440.png", record_pos=(-0.141, -0.029), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547631288153.png", record_pos=(-0.059, -0.207), resolution=(1366, 768)))

sleep(1)
#打包关闭按钮 
poco("com.yhbc.yhz.dinner:id/iv_close").click()


touch(Template(r"tpl1548058687228.png", record_pos=(-0.416, -0.259), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1548055278305.png", record_pos=(-0.366, -0.258), resolution=(1366, 768)))
touch(Template(r"tpl1548055294391.png", record_pos=(0.211, 0.135), resolution=(1366, 768)))
sleep(1.0)

touch(Template(r"tpl1552370125658.png", record_pos=(-0.332, 0.205), resolution=(1366, 768)))

sleep(2.0)
# 抹零小数点
poco("com.yhbc.yhz.dinner:id/rb_erase_other").click()
sleep(1.0)
# poco("com.yhbc.yhz.dinner:id/iv_erase").click()

touch(Template(r"tpl1551419963104.png", record_pos=(0.083, -0.077), resolution=(1366, 768)))
# poco(text="抹零到小数").click()

# poco("com.yhbc.yhz.dinner:id/rb_erase_decimal").click()

touch(Template(r"tpl1548043518507.png", record_pos=(0.403, 0.155), resolution=(1366, 768)))
touch(Template(r"tpl1548058837394.png", record_pos=(0.433, 0.045), resolution=(1366, 768)))
touch(Template(r"tpl1552373065790.png", record_pos=(0.329, 0.207), resolution=(1366, 768)))

sleep(4.0)
# 查看订单
touch(Template(r"tpl1547632610096.png", record_pos=(-0.469, 0.109), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547632628855.png", record_pos=(-0.103, -0.206), resolution=(1366, 768)))
sleep(5.0)
# 验证已结账订单金额是否正确
order_total_price=poco("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/rl_common").child("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/lv_order").offspring("com.yhbc.yhz.dinner:id/tv_buy_price").get_text()

print("order_total_price="+order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("7.0",order_total_price," 订单详情-验证金额总价")

# 验证已结账订单支付方式
pay_mode=poco("com.yhbc.yhz.dinner:id/lv_order").child("com.yhbc.yhz.dinner:id/layout_item")[0].child("com.yhbc.yhz.dinner:id/tv_pay_mode").get_text()
assert_equal("人工现金",pay_mode," 订单详情-验证支付方式=会员卡")
# 验证订单状态
order_state=poco("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/rl_common").child("android.widget.LinearLayout").offspring("com.yhbc.yhz.dinner:id/lv_order").offspring("com.yhbc.yhz.dinner:id/tv_pay_status").get_text()# 获取订单状态值
print("order_state="+order_state)
assert_equal("已结账",order_state," 订单详情-验证反结账之后订单状态")
# 还原桌面
touch(Template(r"tpl1547783142856.png", record_pos=(-0.454, -0.254), resolution=(1366, 768)))


