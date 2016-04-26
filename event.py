#!/usr/bin/python -u
# -*- coding: UTF-8 -*-

import time

print("Content-Type: text/event-stream")
print("Connection: close")
print("")

while 1:
    print("event: ping")
    print("data: Hello World!")
    print("")
    time.sleep(5)
