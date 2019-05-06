#!/usr/bin/env python3
"""
@author = Paolo Grasso
"""

import requests
import json
import time

URL = 'http://0.0.0.0:8080/'


class MyDevice(object):

    def __init__(self):
        self.dict = {
        "type": "device",
        "id": "lamp_1",
        "end-points": ["topic1", "rest1"],
        "res": "dimmering"
        }

    def run(self):
        while True:
            try:
                r = requests.put(URL+'add', data=json.dumps(self.dict))
                print("Status updated")
            except:
                print("Server is unreachable")

            time.sleep(45)


if __name__ == '__main__':
    device = MyDevice()
    device.run()