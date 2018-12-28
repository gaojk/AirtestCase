# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1543395614518.png", record_pos=(-0.219, -0.179), resolution=(1366, 768)))
touch(Template(r"tpl1543395622012.png", record_pos=(0.283, 0.188), resolution=(1366, 768)))
sleep(2.0)
assert_exists(Template(r"tpl1543462396577.png", record_pos=(-0.357, -0.168), resolution=(1366, 768)), "验证付款金额是否准确")

touch(Template(r"tpl1543395665416.png", record_pos=(0.321, 0.12), resolution=(1366, 768)))
sleep(1.0)

snapshot(msg="下单成功截图")



