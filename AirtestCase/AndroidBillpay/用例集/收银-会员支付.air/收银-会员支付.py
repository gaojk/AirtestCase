# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1545986622990.png", record_pos=(-0.224, 0.058), resolution=(1366, 768)))
touch(Template(r"tpl1545987238858.png", record_pos=(0.052, -0.07), resolution=(1366, 768)))


touch(Template(r"tpl1545986699585.png", record_pos=(0.069, 0.156), resolution=(1366, 768)))
snapshot(msg="检验是否现金支付成功！")
assert_equal("付款成功", "付款成功", "检查是否出现付款成功提示.")


