# -*- encoding=utf8 -*-
__author__ = "water"
__title__ = "test script title"
__desc__ = """
this is a test script.
"""

# start your script here
from airtest.core.api import *


# set_logdir("logs")

connect_device("Android:///")

wake()
home()

shell("am force-stop com.gameholic.drawsomethingbyspider")
start_app("com.gameholic.drawsomethingbyspider")
sleep(secs=15.0)

if assert_exists(Template(r"tpl1521885583509.png", record_pos=(0.001, -0.256),
                          resolution=(1440, 2392)), "启动成功"):
    touch(Template(r"tpl1521885626817.png", record_pos=(-0.007, -0.142),
                   resolution=(1440, 2392)))
    touch(Template(r"tpl1521884327086.png", record_pos=(0.287, -0.199),
               resolution=(1440, 2560)))
    touch(Template(r"tpl1521884376802.png", record_pos=(-0.283, -0.193), resolution=(1440.0, 2560.0)))
    touch(Template(r"tpl1521885137253.png", record_pos=(-0.198, -0.136),
                   resolution=(1440, 2392)))
    text("wn10007")
    touch(Template(r"tpl1521884411919.png", record_pos=(-0.169, -0.077), resolution=(1440, 2560)))
    text("z123456")
    touch(Template(r"tpl1521884435349.png", record_pos=(-0.002, 0.053), resolution=(1440, 2560)))
sleep(secs=15.0)
touch(Template(r"tpl1521885236172.png", threshold=0.6, target_pos=5, rgb=True, record_pos=(0.463, -0.793), resolution=(1440, 2392)))
assert_exists(Template(r"tpl1521885529067.png", record_pos=(0.01, -0.112), resolution=(1440, 2392)), "登录成功")
stop_app("com.gameholic.drawsomethingbyspider")
sleep(2)
snapshot(msg="游戏关闭")
print("测试结束")

# simple_report("logs")
