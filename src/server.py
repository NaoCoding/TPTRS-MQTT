import paho.mqtt.client as mqtt
import ssl
import struct
import time , json

to_client = "finalProjectTeam7"
to_server = "Team7finalProject"

def on_connect(client, userdata, flags, rc, properties):
    print("Server is on")
    pass

def on_message(client, userdata, msg):
    try:
        payload_string = [float(x) for x in str(msg.payload, encoding='utf8').split(",")]
    except:
        return
    print(payload_string)
    
    

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("team7", "lkjhgfdsa")
client.connect("140.122.185.98", 1883, 60)
client.subscribe(to_server, 0)
client.loop_forever()