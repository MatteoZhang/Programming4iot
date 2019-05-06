#!/usr/bin/env python3
"""
@author = Paolo Grasso
http://0.0.0.0:8080/?json={%22type%22:%20%22users%22,%22id%22:%20%22001%22}
http://0.0.0.0:8080/?json={%22type%22:%20%22users%22,%22id%22:%20%22all%22}
"""

import paho.mqtt.client as PahoMQTT
import json
import cherrypy
import time
import datetime
import requests
from threading import Thread
from lab5_es1 import *


class MqttCatalog(WebServer):
    pass

if __name__ == '__main__':
    main_thread = MainThread(1)
    #other_thread = OtherThread(2)
    main_thread.start()
    # time.sleep(15)
    # other_thread.start()