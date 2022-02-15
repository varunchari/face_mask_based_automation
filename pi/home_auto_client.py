from threading import Thread, enumerate
import mqttClient
import time
import os
import globals
import datetime
import asyncio
from kasa import SmartPlug

def start_sub(client,topic):
    mqttClient.subscribe(client,topic)
    client.loop_forever()

async def plug_ops():
    if dev.is_on:
        if (("mask_was_worn_incorrectly" in globals.recieved_message) or ("without_mask" in globals.recieved_message)):
            await dev.turn_off()
            await dev.update()
    if dev.is_off:
        if ("with_mask" in globals.recieved_message):
            await dev.turn_on()
            await dev.update()

globals.init()
client = mqttClient.connect_mqtt()
topic = "darknet/predictions"
dev = SmartPlug("192.168.1.68")
asyncio.run(dev.update())
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
            asyncio.run(plug_ops())
        except:
            print("could not write to file")
        globals.recieved_message = ""
file_output.close()
