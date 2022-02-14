# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = '192.168.1.84'
port = 1883
#global recieved_mesasge
#topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = 'client_12345'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client,topic,message):
    result = client.publish(topic, message)
    status = result[0]
    if status == 0:
        print(f"Send `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def subscribe(client,topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        #recieved_message = msg

    client.subscribe(topic)
    client.on_message = on_message

def run():
    #client = connect_mqtt()
    #client.loop_forever()
    #publish(client)
    print("starting mqtt client")


if __name__ == '__main__':
    run()

