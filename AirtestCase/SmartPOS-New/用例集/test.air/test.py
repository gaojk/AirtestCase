# -*- encoding=utf8 -*-
# 场景一：顾客到店，点选“焦糖奶茶-中杯+1元香草”、“波霸奶茶+去冰”、“菠萝啤+打包+打包费1元”。下单后，退掉波霸奶茶，改为“炸鸡腿（称重）+不加辣”，用餐完毕，会员卡结账，享受8折优惠。结账核对账单，

__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
stop_app("com.yhbc.yhz.dinner")
start_app("com.yhbc.yhz.dinner",activity=None)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

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



