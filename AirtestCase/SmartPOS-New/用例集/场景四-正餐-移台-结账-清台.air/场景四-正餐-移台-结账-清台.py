# -*- encoding=utf8 -*-
# 场景：开台-订餐人数2人-下单-现金支付-清台
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
stop_app("com.yhbc.yhz.dinner")
start_app("com.yhbc.yhz.dinner",activity=None)
sleep(4)
touch(Template(r"tpl1551372987427.png", record_pos=(-0.001, -0.013), resolution=(1366, 768)))
sleep(8)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 顾客A操作 
touch(Template(r"tpl1548123887281.png", record_pos=(-0.469, -0.149), resolution=(1366, 768)))
touch(Template(r"tpl1548123922047.png", record_pos=(-0.06, -0.173), resolution=(1366, 768)))

sleep(2.0)
assert_exists(Template(r"tpl1548123982224.png", record_pos=(-0.142, -0.165), resolution=(1366, 768)), "验证是否弹出订单人数选择框")
touch(Template(r"tpl1548124006973.png", record_pos=(0.079, -0.07), resolution=(1366, 768)))
touch(Template(r"tpl1552372219443.png", record_pos=(-0.001, 0.094), resolution=(1366, 768)))

sleep(1)
touch(Template(r"tpl1547630742496.png", record_pos=(0.452, -0.206), resolution=(1366, 768)))
touch(Template(r"tpl1548124051508.png", record_pos=(0.144, -0.253), resolution=(1366, 768)))

sleep(1)
touch(Template(r"tpl1547630868231.png", record_pos=(-0.14, -0.162), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547630884528.png", record_pos=(-0.056, -0.113), resolution=(1366, 768)))
sleep(1)
poco("com.yhbc.yhz.dinner:id/iv_close").click()
sleep(2)
touch(Template(r"tpl1548124130915.png", record_pos=(0.244, -0.251), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547631039247.png", record_pos=(0.158, -0.17), resolution=(1366, 768)))
sleep(1.0)

touch(Template(r"tpl1548124170853.png", record_pos=(-0.246, 0.212), resolution=(1366, 768)))

sleep(2.0)

touch(Template(r"tpl1548124236255.png", record_pos=(-0.064, -0.172), resolution=(1366, 768)))
sleep(2.0)
#    退菜
touch(Template(r"tpl1548124586707.png", record_pos=(-0.372, 0.212), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1548124643502.png", record_pos=(-0.139, 0.089), resolution=(1366, 768)))
touch(Template(r"tpl1548124725426.png", record_pos=(-0.393, -0.126), resolution=(1366, 768)))
touch(Template(r"tpl1548124737502.png", record_pos=(0.09, 0.216), resolution=(1366, 768)))

sleep(1.0)
touch(Template(r"tpl1548124780999.png", record_pos=(-0.247, 0.212), resolution=(1366, 768)))
sleep(3.0)

# 修改人数
touch(Template(r"tpl1548124236255.png", record_pos=(-0.064, -0.172), resolution=(1366, 768)))

touch(Template(r"tpl1548125039592.png", record_pos=(-0.141, -0.184), resolution=(1366, 768)))
touch(Template(r"tpl1548125058953.png", record_pos=(-0.053, -0.053), resolution=(1366, 768)))
touch(Template(r"tpl1548125069243.png", record_pos=(-0.048, -0.17), resolution=(1366, 768)))
touch(Template(r"tpl1548125079026.png", record_pos=(0.037, 0.217), resolution=(1366, 768)))
sleep(1.0)

touch(Template(r"tpl1548125184619.png", record_pos=(-0.143, -0.255), resolution=(1366, 768)))
touch(Template(r"tpl1548125196336.png", record_pos=(-0.195, -0.092), resolution=(1366, 768)))
touch(Template(r"tpl1548125203629.png", record_pos=(0.043, 0.134), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1548125230886.png", record_pos=(-0.065, -0.251), resolution=(1366, 768)))

# 顾客B操作 
# touch(Template(r"tpl1548125346557.png", record_pos=(-0.471, -0.203), resolution=(1366, 768)))

sleep(2.0)
touch(Template(r"tpl1548125410510.png", record_pos=(0.041, -0.25), resolution=(1366, 768)))

assert_exists(Template(r"tpl1548123982224.png", record_pos=(-0.142, -0.165), resolution=(1366, 768)), "验证是否弹出订单人数选择框")
touch(Template(r"tpl1548125471751.png", record_pos=(0.001, -0.07), resolution=(1366, 768)))
touch(Template(r"tpl1552372219443.png", record_pos=(-0.001, 0.094), resolution=(1366, 768)))

sleep(1)
touch(Template(r"tpl1547631039247.png", record_pos=(0.158, -0.17), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1548125521186.png", record_pos=(0.045, -0.251), resolution=(1366, 768)))

sleep(1.0)
touch(Template(r"tpl1548125553333.png", record_pos=(-0.25, 0.212), resolution=(1366, 768)))
sleep(1.0)


#服务员加错菜到B1
touch(Template(r"tpl1548125230886.png", record_pos=(-0.065, -0.251), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1548125621326.png", record_pos=(-0.37, 0.21), resolution=(1366, 768)))
sleep(2.0)

touch(Template(r"tpl1548125740826.png", record_pos=(0.246, -0.247), resolution=(1366, 768)))
touch(Template(r"tpl1548125768964.png", record_pos=(-0.247, 0.213), resolution=(1366, 768)))

sleep(2.0)

touch(Template(r"tpl1548125812926.png", record_pos=(-0.07, -0.25), resolution=(1366, 768)))

touch(Template(r"tpl1548125621326.png", record_pos=(-0.37, 0.21), resolution=(1366, 768)))
sleep(1.0)

touch(Template(r"tpl1548126017224.png", record_pos=(-0.14, 0.124), resolution=(1366, 768)))
touch(Template(r"tpl1552372648861.png", record_pos=(0.012, -0.162), resolution=(1366, 768)))

touch(Template(r"tpl1548126078611.png", record_pos=(-0.201, -0.089), resolution=(1366, 768)))
touch(Template(r"tpl1548126086400.png", record_pos=(0.045, 0.123), resolution=(1366, 768)))
touch(Template(r"tpl1548126100510.png", record_pos=(0.089, 0.212), resolution=(1366, 768)))
touch(Template(r"tpl1548126298864.png", record_pos=(-0.247, 0.212), resolution=(1366, 768)))
sleep(1.0)

# B1结账------------------------------
touch(Template(r"tpl1548127365168.png", record_pos=(-0.065, -0.253), resolution=(1366, 768)))
touch(Template(r"tpl1548127126999.png", record_pos=(-0.247, 0.212), resolution=(1366, 768)))
# 点击订单折扣
poco("com.yhbc.yhz.dinner:id/et_discount").click()
touch(Template(r"tpl1548127703165.png", record_pos=(0.367, -0.01), resolution=(1366, 768)))
touch(Template(r"tpl1552373840993.png", record_pos=(0.329, 0.209), resolution=(1366, 768)))

sleep(3.0)
# 查看B1订单

# 验证已结账订单金额是否正确
# b1order_total_price=poco("com.yhbc.yhz.dinner:id/tv_buy_price").get_text()

# print("b1order_total_price="+b1order_total_price)
# # 打包盒、餐具费不参与打折
# assert_equal("共4份，合计7.8元",b1order_total_price," B1订单详情-验证金额总价")
# touch(Template(r"tpl1547783142856.png", record_pos=(-0.454, -0.254), resolution=(1366, 768)))
# sleep(2.0)
# B1清台
touch(Template(r"tpl1548123887281.png", record_pos=(-0.469, -0.149), resolution=(1366, 768)))
touch(Template(r"tpl1548136343906.png", record_pos=(-0.061, -0.253), resolution=(1366, 768)))
touch(Template(r"tpl1548127346024.png", record_pos=(-0.141, -0.097), resolution=(1366, 768)))
sleep(3)
touch(Template(r"tpl1548127356434.png", record_pos=(0.044, 0.071), resolution=(1366, 768)))
sleep(3)

# B2结账------------------------
touch(Template(r"tpl1548127113183.png", record_pos=(0.042, -0.25), resolution=(1366, 768)))
sleep(3)
touch(Template(r"tpl1548127126999.png", record_pos=(-0.247, 0.212), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1552373065790.png", record_pos=(0.329, 0.207), resolution=(1366, 768)))

sleep(3.0)
# 查看B2订单
touch(Template(r"tpl1547632610096.png", record_pos=(-0.469, 0.109), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547632628855.png", record_pos=(-0.103, -0.206), resolution=(1366, 768)))
sleep(2.0)
# 验证已结账订单金额是否正确
b2order_total_price=poco("com.yhbc.yhz.dinner:id/tv_buy_price").get_text()
print("b2order_total_price="+b2order_total_price)
# 打包盒、餐具费不参与打折
assert_equal("23.0",b2order_total_price," 订单详情-验证金额总价")
touch(Template(r"tpl1547783142856.png", record_pos=(-0.454, -0.254), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1548123887281.png", record_pos=(-0.469, -0.149), resolution=(1366, 768)))
touch(Template(r"tpl1548136106172.png", record_pos=(0.045, -0.25), resolution=(1366, 768)))
# B2清台
touch(Template(r"tpl1548127346024.png", record_pos=(-0.141, -0.097), resolution=(1366, 768)))
sleep(3)
touch(Template(r"tpl1548127356434.png", record_pos=(0.044, 0.071), resolution=(1366, 768)))
sleep(1)
