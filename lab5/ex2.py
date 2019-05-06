#!/usr/bin/env python3
"""
@author = Paolo Grasso
"""

import requests
import json

URL = 'http://0.0.0.0:8080/'

class MyApplication(object):
    def __init__(self):
        print("Connetting to the Moon...")

    def run(self):
        while True:
            print("What do you want to do?")
            print("1) the message broker")
            print("2) all the registered devices")
            print("3) device with a specific deviceID given as input")
            print("4) all the registered users")
            print("5) device with a specific userID given as input")
            inp = input("> ")

            if inp == '1':
                j = '?json={"type": "broker"}'
                r = requests.get(URL+j)
                try:
                    res = json.loads(r.text)
                    print('\nIP address:', res['ip'])
                    print('port: ', res['port'],'\n')
                except:
                    print("\nHTTP Error:", r.status_code, "\n")

            if inp == '2':
                j = '?json={"type": "devices", "id": "all"}'
                r = requests.get(URL+j)
                try:
                    res = json.loads(r.text)
                    print("")
                    print(json.dumps(res, indent=2))
                    print("")
                except:
                    print("\nHTTP Error:", r.status_code, "\n")

            if inp == '3':
                id = input("Type the deviceID >")
                dict = json.dumps({"type": "devices", "id": id})
                j = '?json='+dict
                r = requests.get(URL+j)
                try:
                    res = json.loads(r.text)
                    print("")
                    print(json.dumps(res, indent=2))
                    print("")
                except:
                    print("\nHTTP Error:", r.status_code, "\n")

            if inp == '4':
                j = '?json={"type": "users", "id": "all"}'
                r = requests.get(URL+j)
                res = json.loads(r.text)
                try:
                    print("")
                    print(json.dumps(res, indent=2))
                    print("")
                except:
                    print("\nHTTP Error:", r.status_code, "\n")

            if inp == '5':
                id = input("Type the userID >")
                dict = json.dumps({"type": "users", "id": id})
                j = '?json='+dict
                r = requests.get(URL+j)
                try:
                    res = json.loads(r.text)
                    print("")
                    print(json.dumps(res, indent=2))
                    print("")
                except:
                    print("\nHTTP Error:", r.status_code, "\n")


if __name__ == '__main__':
    app = MyApplication()
    app.run()