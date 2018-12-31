# -*- encoding=utf8 -*-
# 场景：开台-订餐人数2人-下单-现金支付-清台
__author__ = "lsd"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
touch(Template(r"tpl1546062477694.png", record_pos=(-0.348, -0.064), resolution=(1366, 768)))
sleep(2.0)
assert_exists(Template(r"tpl1545989483597.png", record_pos=(0.0, -0.17), resolution=(1366, 768)), "验证是否弹出订单人数选择框")

touch(Template(r"tpl1545988828587.png", record_pos=(0.002, -0.063), resolution=(1366, 768)))
touch(Template(r"tpl1545988840243.png", record_pos=(-0.002, 0.098), resolution=(1366, 768)))
wait(Template(r"tpl1546063310124.png", record_pos=(-0.318, -0.15), resolution=(1366, 768)))
touch(Template(r"tpl1546077516867.png", record_pos=(-0.223, 0.011), resolution=(1366, 768)))

#touch(Template(r"tpl1546062508928.png", record_pos=(-0.34, 0.012), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1545988897393.png", record_pos=(0.425, 0.221), resolution=(1366, 768)))
sleep(3.0)
touch(Template(r"tpl1545988912844.png", record_pos=(0.316, 0.121), resolution=(1366, 768)))
sleep(2.0)
touch(Template(r"tpl1546063268698.png", record_pos=(-0.253, -0.236), resolution=(1366, 768)))
assert_not_exists(Template(r"tpl1546078213914.png", record_pos=(-0.305, -0.045), resolution=(1366, 768)), "验证桌台B6是否已结帐")

touch(Template(r"tpl1546063094189.png", record_pos=(-0.352, -0.067), resolution=(1366, 768)))


assert_exists(Template(r"tpl1545989062860.png", record_pos=(0.371, -0.125), resolution=(1366, 768)), "验证餐具费是否正确2元")
assert_exists(Template(r"tpl1545989111213.png", record_pos=(0.439, 0.162), resolution=(1366, 768)), "验证订单，共2项，合计7元")

touch(Template(r"tpl1545989072507.png", record_pos=(0.43, 0.216), resolution=(1366, 768)))
assert_exists(Template(r"tpl1545989148658.png", record_pos=(0.001, -0.018), resolution=(1366, 768)), "验证是否弹出清台提示框")
touch(Template(r"tpl1545989156526.png", record_pos=(0.063, 0.033), resolution=(1366, 768)))
sleep(1.0)
assert_exists(Template(r"tpl1546063122877.png", record_pos=(-0.352, -0.055), resolution=(1366, 768)), "验证b6桌台是清台成功，状态=空闲")

