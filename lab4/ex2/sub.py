import paho.mqtt.client as PahoMQTT
import time

#broker = 'test.mosquitto.org'
#broker = 'broker.hivmq.com'
#broker = 'iot.eclipse.org'
#broker = '192.168.43.220'
IPv4 = '192.168.43.178'


class MySubscriber:
    def __init__(self, clientID):
        self.clientID = clientID

        # create an instance of paho.mqtt.client
        self._paho_mqtt = PahoMQTT.Client(self.clientID, False)
        # register the callback
        self._paho_mqtt.on_connect = self.myOnConnect
        self._paho_mqtt.on_message = self.myOnMessageReceived
        self.topic = '/unix'
        self.messageBroker = IPv4

    def start(self):
        #manage connection to broker
        self._paho_mqtt.connect(self.messageBroker, 1883)
        self._paho_mqtt.loop_start()
        self._paho_mqtt.subscribe(self.topic, 2)

    def stop(self):
        self._paho_mqtt.unsubscribe(self.topic)
        self._paho_mqtt.loop_stop()
        self._paho_mqtt.disconnect()

    def myOnConnect (self, paho_mqtt, userdata, flags, rc):
        print ("Connected to %s with result code: %d" % (self.messageBroker, rc))

    def myOnMessageReceived(self, paho_mqtt, userdata, msg):
        print ("Topic: '" + msg.topic + "', Qos: '" + str(msg.qos) + "' Message: '" + str(msg.payload) + "'")

if __name__ == "__main__":
    test = MySubscriber("MySubscriber 1")
    test.start()

    while True:
        time.sleep(1)

    test.stop()

# TODO user friendly json format