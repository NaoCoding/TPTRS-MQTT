# TPTRS-MQTT

[TPTRS-MQTT](https://github.com/NaoCoding/TPTRS-MQTT) is a project written with **PyQt5** and **MQTT** server, <br> the final project of [Data Science &amp; Communication 2024](https://web.ntnu.edu.tw/~cw/icoil/) NTNU. <br><br>

The default setting of the MQTT broker located at **NTNU**(National Taiwan Normal University), <br>however we can't assume that the MQTT broker will keep working after the course ended.<br><br>

To run the server with your own MQTT broker, edit the IP address in **server.py** and **client_mqtt.py**.

---

### PyQt5

- [x] **Web Engine** for interacting Folium Map
- [x] Graphic User Interface for better experience
- [x] Select Language options for different language users ( **English** , **Traditional Chinese** , **Japanese**(partial) )

 ### Folium

 - [x] Support **OpenStreetMap** and other tiles.
 - [x] automatically generate markers from real-time api data
 - [x] MarkerCluster and markers for **MRT**, **bus**, and **Ubike** stations

### MQTT

- [x] MQTT server for clients to interact data
- [x] Support localhost and MQTT brokers

