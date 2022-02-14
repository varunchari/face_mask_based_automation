from threading import Thread, enumerate
import mqttClient
import time
import os
import globals
import datetime

def start_sub(client,topic):
    mqttClient.subscribe(client,topic)
    client.loop_forever()

globals.init()
client = mqttClient.connect_mqtt()
topic = "darknet/predictions"
Thread(target=start_sub, args=(client,topic)).start()

try:
    file_output = open("output/results.txt", "w+")
except:
    print("unable to open file")

while True:
    time.sleep(1)
    if(globals.recieved_message != ""):
        cur_time = datetime.datetime.now()
        try:
            file_output.write(str(cur_time) + ":" + globals.recieved_message + "\n")
            file_output.flush()
        except:
            print("could not write to file")
        globals.recieved_message = ""
file_output.close()
