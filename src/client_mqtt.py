import paho.mqtt.client as mqtt
import ssl
import struct
import time

class _client:
    
    def __init__(self) -> None:
        
        self.to_server = "Team7finalProject"
        self.to_client = "finalProjectTeam7"

        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.username_pw_set("team7", "lkjhgfdsa")
        self.client.connect("140.122.185.98", 1883, 60)

        self.client.loop_start()



    def on_connect(self, client, userdata, flags, rc, properties):
        self.client.subscribe(self.to_client, 0)

    def on_message(self , client, userdata, msg):
        message = str(msg.payload, encoding='utf8')
        s = message

    def action(self , msg):
        self.client.publish(self.to_server, msg, 0)
    

_mqtt = _client()


