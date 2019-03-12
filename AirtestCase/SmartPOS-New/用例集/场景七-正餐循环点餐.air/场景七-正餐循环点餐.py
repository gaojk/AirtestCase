# -*- encoding=utf8 -*-
__author__ = "lsd"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
# stop_app("com.yhbc.yhz.dinner")
# start_app("com.yhbc.yhz.dinner",activity=None)
# sleep(3)
# touch(Template(r"tpl1551372987427.png", record_pos=(-0.001, -0.013), resolution=(1366, 768)))
# sleep(8)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
loop_num=1  #循环次数
for i in range(loop_num):
    i=i+1
    print("单脚本中循环次数i="+str(i))

    # 顾客A操作 
    touch(Template(r"tpl1551064173368.png", record_pos=(-0.469, -0.147), resolution=(1366, 768)))
    touch(Template(r"tpl1551064196965.png", record_pos=(0.041, -0.093), resolution=(1366, 768)))

    sleep(2.0)
    touch(Template(r"tpl1551064219936.png", record_pos=(-0.004, -0.07), resolution=(1366, 768)))
    touch(Template(r"tpl1551064240675.png", record_pos=(0.001, 0.102), resolution=(1366, 768)))
    sleep(1)
    touch(Template(r"tpl1551064283338.png", record_pos=(0.456, -0.208), resolution=(1366, 768)))
    sleep(1)
    touch(Template(r"tpl1547631039247.png", record_pos=(0.158, -0.17), resolution=(1366, 768)))
    sleep(1)
    # 打包 
    touch(Template(r"tpl1547631244440.png", record_pos=(-0.141, -0.029), resolution=(1366, 768)))
    sleep(1)
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
    sleep(1)

#     # 验证属性是否增加显示
#     prop=poco("com.yhbc.yhz.dinner:id/tv_property").get_text()
#     assert_equal("+蓝莓+去冰",prop,"属性显示=+蓝莓+去冰")
    touch(Template(r"tpl1551064332145.png", record_pos=(-0.369, 0.212), resolution=(1366, 768)))
    sleep(1.0)
    touch(Template(r"tpl1551064365790.png", record_pos=(-0.037, 0.012), resolution=(1366, 768)))
    sleep(1.0)
#     touch(Template(r"tpl1548054202672.png", record_pos=(0.335, 0.214), resolution=(1366, 768)))
    touch(Template(r"tpl1552359826417.png", record_pos=(0.327, 0.21), resolution=(1366, 768)))

    
    sleep(2.0)
    touch(Template(r"tpl1551064728167.png", record_pos=(0.04, -0.092), resolution=(1366, 768)))
    touch(Template(r"tpl1551064754717.png", record_pos=(-0.138, -0.098), resolution=(1366, 768)))
    touch(Template(r"tpl1551064764767.png", record_pos=(0.042, 0.07), resolution=(1366, 768)))
    sleep(1.0)









