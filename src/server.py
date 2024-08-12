import paho.mqtt.client as mqtt
import ssl
import struct
import time , json , requests , csv

to_client = "finalProjectTeam7"
to_server = "Team7finalProject"

INF = 10**9


def _dist(a , b , c , d):

    return (c-a)**2 + (d-b)**2

def on_connect(client, userdata, flags, rc, properties):
    print("Server is on")
    pass

def on_message(client, userdata, msg):

    try: lat , lng = [float(x) for x in str(msg.payload, encoding='utf8').split(",")]
    except: return

    return_string = f"_{_MRT_(lat , lng)}_{_UBIKE_(lat , lng)}_{_BUS_(lat , lng)}"

    client.publish(to_client, return_string)
    

def _MRT_(lat , lng):

    data = list(csv.reader(
                requests.get(
                    "https://raw.githubusercontent.com/repeat/northern-taiwan-metro-stations/master/northern-taiwan.csv"
                ).content.decode("utf-8").splitlines() , delimiter=','
            ))[1:]

    for i in range(len(data)): data[i][7] , data[i][8] = float(data[i][7]) , float(data[i][8])

    near = [0,0,0]

    dd = [INF , INF , INF]

    for i in range(len(data)):

        if data[i][2] in [data[x][2] for x in near]:
            continue

        if _dist(lat , lng , data[i][7] , data[i][8]) < dd[-1]:
            if _dist(lat , lng , data[i][7] , data[i][8]) < dd[-2]:
                if _dist(lat , lng , data[i][7] , data[i][8]) < dd[-3]:
                    dd = [_dist(lat , lng , data[i][7] , data[i][8])] + dd[:2]
                    near = [i] + near[:2]
                else:
                    dd = [dd[0]] + [_dist(lat , lng , data[i][7] , data[i][8])] + [dd[1]]
                    near = [near[0]] + [i] + [near[1]]
            else:
                dd = dd[:2] + [_dist(lat , lng , data[i][7] , data[i][8])]
                near = near[:2] + [i]
        else:
            continue

    return ",".join([str(x) for x in near])
    #print(near , dd)
    


    
def _UBIKE_(lat , lng):
    
    data = requests.get(
            "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
        ).json()

    near = [0,0,0]

    dd = [INF , INF , INF]

    for i in range(len(data)):


        if _dist(lat , lng , data[i]['latitude'] , data[i]['longitude']) < dd[-1]:
            if _dist(lat , lng , data[i]['latitude'] , data[i]['longitude']) < dd[-2]:
                if _dist(lat , lng , data[i]['latitude'] , data[i]['longitude']) < dd[-3]:
                    dd = [_dist(lat , lng , data[i]['latitude'] , data[i]['longitude'])] + dd[:2]
                    near = [i] + near[:2]
                else:
                    dd = [dd[0]] + [_dist(lat , lng , data[i]['latitude'] , data[i]['longitude'])] + [dd[1]]
                    near = [near[0]] + [i] + [near[1]]
            else:
                dd = dd[:2] + [_dist(lat , lng , data[i]['latitude'] , data[i]['longitude'])]
                near = near[:2] + [i]
        else:
            continue

    #print(near)
    return ",".join([str(x) for x in near])


def _BUS_(lat , lng):
    
    data = requests.get(
            "https://github.andy-lu.dev/hide_api/taipei_bus.json"
        ).json()['features']

    near = [0,0,0]

    dd = [INF , INF , INF]

    for i in range(len(data)):


        if _dist(lat , lng , data[i]['geometry']['coordinates'][1] , 
                 data[i]['geometry']['coordinates'][0]) < dd[-1]:
            if _dist(lat , lng , data[i]['geometry']['coordinates'][1] , 
                 data[i]['geometry']['coordinates'][0]) < dd[-2]:
                if _dist(lat , lng , data[i]['geometry']['coordinates'][1] , 
                 data[i]['geometry']['coordinates'][0]) < dd[-3]:
                    dd = [_dist(lat , lng , data[i]['geometry']['coordinates'][1] , 
                 data[i]['geometry']['coordinates'][0])] + dd[:2]
                    near = [i] + near[:2]
                else:
                    dd = [dd[0]] + [_dist(lat , lng , data[i]['geometry']['coordinates'][1] , 
                 data[i]['geometry']['coordinates'][0])] + [dd[1]]
                    near = [near[0]] + [i] + [near[1]]
            else:
                dd = dd[:2] + [_dist(lat , lng , data[i]['geometry']['coordinates'][1] , 
                 data[i]['geometry']['coordinates'][0])]
                near = near[:2] + [i]
        else:
            continue

    #print(near)
    return ",".join([str(x) for x in near])
    
    

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("team7", "lkjhgfdsa")
client.connect("140.122.185.98", 1883, 60)
client.subscribe(to_server, 0)
client.loop_forever()