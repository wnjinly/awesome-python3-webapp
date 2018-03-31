# -*- encoding=utf8 -*-
__author__ = "water"
__title__ = "test script title"
__desc__ = """
this is a test script.
"""

# start your script here
connect_device("Android:///")
wake()
home()
shell("am ")
start_app("com.gameholic.drawsomethingbyspider")
