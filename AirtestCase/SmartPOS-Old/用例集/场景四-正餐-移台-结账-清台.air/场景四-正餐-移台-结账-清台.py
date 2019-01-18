# -*- encoding=utf8 -*-
# 场景：开台-订餐人数2人-下单-现金支付-清台
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 顾客A操作 
touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
touch(Template(r"tpl1546062477694.png", record_pos=(-0.348, -0.064), resolution=(1366, 768)))
sleep(2.0)
assert_exists(Template(r"tpl1545989483597.png", record_pos=(0.0, -0.17), resolution=(1366, 768)), "验证是否弹出订单人数选择框")

touch(Template(r"tpl1547190410946.png", record_pos=(0.083, -0.061), resolution=(1366, 768)))

touch(Template(r"tpl1545988840243.png", record_pos=(-0.002, 0.098), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546934613612.png", record_pos=(-0.444, -0.143), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546077516867.png", record_pos=(-0.223, 0.011), resolution=(1366, 768)))

touch(Template(r"tpl1547190487831.png", record_pos=(0.311, -0.111), resolution=(1366, 768)))

sleep(2)

touch(Template(r"tpl1546499359252.png", record_pos=(-0.1, -0.156), resolution=(1366, 768)))
touch(Template(r"tpl1546499377959.png", record_pos=(-0.239, 0.198), resolution=(1366, 768)))

sleep(2.0)
touch(Template(r"tpl1546521088095.png", record_pos=(-0.329, 0.107), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547190526980.png", record_pos=(0.117, -0.176), resolution=(1366, 768)))

touch(Template(r"tpl1547190696232.png", record_pos=(0.28, 0.221), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547198784515.png", record_pos=(-0.338, -0.235), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547198882396.png", record_pos=(-0.333, -0.064), resolution=(1366, 768)))

sleep(2.0)

# 验证桌b6订单金额是否正确
b6_total_price=poco("com.yhbc.tablet:id/countTextView").get_text()

assert_equal("共4项，合计42.00元",b6_total_price,"b6金额是否=42.0")     
     
touch(Template(r"tpl1547190778569.png", record_pos=(0.43, 0.173), resolution=(1366, 768)))
sleep(1.0)
poco("com.yhbc.tablet:id/lv_OrderItem").child("com.yhbc.tablet:id/rl_resting_orderitem_popu")[1].child("android.widget.LinearLayout").child("com.yhbc.tablet:id/chooseImageView").click()
poco("com.yhbc.tablet:id/lv_OrderItem").child("com.yhbc.tablet:id/rl_resting_orderitem_popu")[2].child("android.widget.LinearLayout").child("com.yhbc.tablet:id/chooseImageView").click()
touch(Template(r"tpl1547190986727.png", record_pos=(-0.058, 0.135), resolution=(1366, 768)))
sleep(1.0)
assert_exists(Template(r"tpl1547191055886.png", record_pos=(-0.002, -0.007), resolution=(1366, 768)), "弹出却确认退菜提示框")
touch(Template(r"tpl1547191091481.png", record_pos=(0.04, 0.064), resolution=(1366, 768)))
assert_exists(Template(r"tpl1547191123326.png", record_pos=(-0.001, 0.017), resolution=(1366, 768)), "退菜菜品显示")

poco("android.widget.ImageView").click()
sleep(1.0)
touch(Template(r"tpl1547191233243.png", record_pos=(-0.341, -0.064), resolution=(1366, 768)))
# 验证订单金额
sleep(2.0)
total_price=poco("com.yhbc.tablet:id/countTextView").get_text()


assert_equal("共4项，合计15.00元",total_price," 验证总计金额=15.00")

touch(Template(r"tpl1547191335373.png", record_pos=(0.458, -0.189), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547191363463.png", record_pos=(-0.082, -0.061), resolution=(1366, 768)))
touch(Template(r"tpl1547191374677.png", record_pos=(-0.001, 0.098), resolution=(1366, 768)))

# 验证订单金额
after_xgrs_total_price=poco("com.yhbc.tablet:id/countTextView").get_text()
assert_equal("共4项，合计13.00元",after_xgrs_total_price,"验证总计金额=13.00")
touch(Template(r"tpl1547191552487.png", record_pos=(0.283, 0.127), resolution=(1366, 768)))
sleep(2)
assert_exists(Template(r"tpl1547191634164.png", record_pos=(-0.316, -0.048), resolution=(1366, 768)), "验证显示移台标识")

touch(Template(r"tpl1547192202777.png", record_pos=(-0.35, -0.143), resolution=(1366, 768)))
sleep(2)
touch(Template(r"tpl1547199703555.png", record_pos=(-0.335, -0.143), resolution=(1366, 768)))
sleep(2)
# 验证移台后金额 
after_ytb1_total_price=poco("com.yhbc.tablet:id/countTextView").get_text()
assert_equal(after_xgrs_total_price,after_ytb1_total_price,"验证总计金额=13.00")

# 顾客B操作 
touch(Template(r"tpl1547198784515.png", record_pos=(-0.338, -0.235), resolution=(1366, 768)))
sleep(2.0)

touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
touch(Template(r"tpl1547192512083.png", record_pos=(-0.228, -0.142), resolution=(1366, 768)))
sleep(2.0)
assert_exists(Template(r"tpl1545989483597.png", record_pos=(0.0, -0.17), resolution=(1366, 768)), "验证是否弹出订单人数选择框")
touch(Template(r"tpl1547192526662.png", record_pos=(-0.002, -0.062), resolution=(1366, 768)))

touch(Template(r"tpl1545988840243.png", record_pos=(-0.002, 0.098), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1546934613612.png", record_pos=(-0.444, -0.143), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547192586570.png", record_pos=(0.011, -0.082), resolution=(1366, 768)))
sleep(1)
touch(Template(r"tpl1547192599266.png", record_pos=(-0.109, -0.174), resolution=(1366, 768)))
# # 验证购物车中订单金额是否正确
# custom2_total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
# assert_equal("13.0",custom2_total_price,"验证商品+打包费金额是否=13.0")
sleep(1.0)
touch(Template(r"tpl1547190696232.png", record_pos=(0.28, 0.221), resolution=(1366, 768)))
sleep(1.0)

#服务员加错菜到B1
touch(Template(r"tpl1547198784515.png", record_pos=(-0.338, -0.235), resolution=(1366, 768)))
sleep(2.0)

touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547192788537.png", record_pos=(-0.344, -0.143), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547192808369.png", record_pos=(0.303, 0.214), resolution=(1366, 768)))
sleep(2.0)
# 错加雪梨汁
poco("com.yhbc.tablet:id/lv_order").child("android.widget.LinearLayout")[0].child("com.yhbc.tablet:id/rl").child("com.yhbc.tablet:id/ll").child("com.yhbc.tablet:id/rl_increase").child("com.yhbc.tablet:id/tv_increase").click()

sleep(1.0)
# 验证加错台购物车中订单金额是否正确
jc_total_price=poco("com.yhbc.tablet:id/tv_total").get_text()
assert_equal("25.0",jc_total_price,"验证商品+打包费金额是否=25.0")
touch(Template(r"tpl1547190696232.png", record_pos=(0.28, 0.221), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547198784515.png", record_pos=(-0.338, -0.235), resolution=(1366, 768)))
sleep(2.0)

touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1547201696576.png", record_pos=(-0.345, -0.139), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547193094893.png", record_pos=(0.367, 0.129), resolution=(1366, 768)))
sleep(2.0)
# 选择转菜菜品 

poco("com.yhbc.tablet:id/rc_content").child("com.yhbc.tablet:id/rl_item")[0].child("com.yhbc.tablet:id/chb_item").click()

touch(Template(r"tpl1547193139196.png", record_pos=(0.058, 0.178), resolution=(1366, 768)))
sleep(1.0)

touch(Template(r"tpl1547193179663.png", record_pos=(-0.229, -0.123), resolution=(1366, 768)))
touch(Template(r"tpl1547193196981.png", record_pos=(0.049, 0.177), resolution=(1366, 768)))
sleep(1.0)
# 验证转菜后b1金额 
after_zc_total_price=poco("com.yhbc.tablet:id/countTextView").get_text()
assert_equal("共4项，合计13.00元",after_zc_total_price,"验证b1总计金额=13.00")

touch(Template(r"tpl1547198784515.png", record_pos=(-0.338, -0.235), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
sleep(1.0)

touch(Template(r"tpl1547193542664.png", record_pos=(-0.22, -0.143), resolution=(1366, 768)))
sleep(2.0)
# 验证转菜后b2金额 
after_zcb2_total_price=poco("com.yhbc.tablet:id/countTextView").get_text()
assert_equal("共4项，合计25.00元",after_zcb2_total_price,"验证b2总计金额=25.00")

touch(Template(r"tpl1547264143371.png", record_pos=(0.428, 0.214), resolution=(1366, 768)))

sleep(2.0)
touch(Template(r"tpl1547193759297.png", record_pos=(0.312, 0.119), resolution=(1366, 768)))
sleep(3.0)
# 验证b2结账后订单金额
b2jz_total_price=poco("com.yhbc.tablet:id/countTextView").get_text()
assert_equal(after_zcb2_total_price,b2jz_total_price," 验证b2结账后订单金额=25元")

touch(Template(r"tpl1545989072507.png", record_pos=(0.43, 0.216), resolution=(1366, 768)))
sleep(1.0)
assert_exists(Template(r"tpl1545989148658.png", record_pos=(0.001, -0.018), resolution=(1366, 768)), "验证是否弹出清台提示框")
touch(Template(r"tpl1545989156526.png", record_pos=(0.063, 0.033), resolution=(1366, 768)))
sleep(2.0)
b2_stat=poco("com.yhbc.tablet:id/gv_menu").child("android.widget.RelativeLayout")[1].child("com.yhbc.tablet:id/rl_item").child("android.widget.LinearLayout").child("com.yhbc.tablet:id/tv_state").get_text()
assert_equal("空闲",b2_stat," 验证B2桌台清台是否成功")
touch(Template(r"tpl1547198784515.png", record_pos=(-0.338, -0.235), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547194055431.png", record_pos=(-0.35, -0.141), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547264143371.png", record_pos=(0.428, 0.214), resolution=(1366, 768)))
sleep(1.0)
poco("com.yhbc.tablet:id/et_discount").click()

# touch(Template(r"tpl1547194275653.png", record_pos=(-0.227, -0.038), resolution=(1366, 768)))
sleep(1.0)
touch(Template(r"tpl1547194285917.png", record_pos=(0.245, -0.012), resolution=(1366, 768)))

sleep(1.0)
touch(Template(r"tpl1547193759297.png", record_pos=(0.312, 0.119), resolution=(1366, 768)))
sleep(3.0)
# 验证b1订单金额
b1jz_total_price=poco("com.yhbc.tablet:id/countTextView").get_text()
assert_equal("共4项，合计7.80元",b1jz_total_price," 验证b1订单金额=7.80元")

touch(Template(r"tpl1545989072507.png", record_pos=(0.43, 0.216), resolution=(1366, 768)))
sleep(1.0)
assert_exists(Template(r"tpl1545989148658.png", record_pos=(0.001, -0.018), resolution=(1366, 768)), "验证是否弹出清台提示框")
touch(Template(r"tpl1545989156526.png", record_pos=(0.063, 0.033), resolution=(1366, 768)))
sleep(2.0)
b1_stat=poco("com.yhbc.tablet:id/gv_menu").child("android.widget.RelativeLayout")[0].child("com.yhbc.tablet:id/rl_item").child("android.widget.LinearLayout").child("com.yhbc.tablet:id/tv_state").get_text()
assert_equal("空闲",b1_stat," 验证B1桌台清台是否成功")

