#!/usr/bin/env python3
"""
@author = Paolo Grasso
"""

import paho.mqtt.client as PahoMQTT
import time
import datetime
import json
import requests
URL = 'http://0.0.0.0:8080'

class MyPublisher(object):
    def __init__(self, clientID, serverIP):
        self.clientID = clientID
        self.messageBroker = serverIP
        self._paho_mqtt = PahoMQTT.Client(self.clientID, False)
        self._paho_mqtt.on_connect = self.my_on_connect  # Association

    def start(self):
        self._paho_mqtt.connect(self.messageBroker, 1883)
        self._paho_mqtt.loop_start()

    def stop(self):
        self._paho_mqtt.loop_stop()
        self._paho_mqtt.disconnect()

    def my_publish(self, topic, message):
        self._paho_mqtt.publish(topic, message, 2)

    def my_on_connect(self, client, userdata, flags, rc):
        global loop_flag
        print ("Connected to %s - Result code: %d" % (self.messageBroker, rc))
        loop_flag = 0


if __name__ == "__main__":
    j = '?json={"type": "broker"}'
    r = requests.get(URL+j)
    res = json.loads(r.text)
    broker_ip = res['ip']
    pub = MyPublisher("Pub1", BROKER_IP)
    loop_flag = 1
    flag = 1
    pub.start()

    while loop_flag:
        print("Waiting for connection...")
        time.sleep(.01)

    while True:
        self.dict = {
        "type": "device",
        "id": "lamp_2",
        "end-points": ["topic1", "rest1"],
        "res": ["dimmering", "color"]
        }
        pub.my_publish('/devices', self.dict)
        time.sleep(30)

    pub.stop()