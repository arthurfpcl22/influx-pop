import random
import time    
from datetime import datetime
from paho.mqtt import client as mqtt_client
from influxdb import InfluxDBClient
import time    
from datetime import datetime


user = 'root'
password = 'root'
dbname = 'teste3'
dbuser = 'isau'
dbuser_password = 'my_secret_password'
hostname = 'localhost'
port = 8086

client2 = InfluxDBClient(host= hostname, port=port, database=dbname)

#client.create_database('teste3')

client2.switch_database('teste3')


broker = '192.168.70.70'
port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(msg.payload.decode().replace("messages: ",""))
        msg = float(msg.payload.decode().replace("messages: ",""))
        now = time.time()

        print(now)

        dt = datetime.fromtimestamp( now )

        d = dt.strftime("%m/%d/%Y, %H:%M:%S")
        d= d.replace(", ", "T").replace("/", "-", 2)+'Z'
        json_body = [
            {
                "measurement": "teste_escrita",
                "tags": {
                    "local": "pop-rn"
                },
                "time": d,
                "fields": {
                    "duration": msg
                }
            }
        ]

        #client.switch_user(dbuser, dbuser_password)

        client2.write_points(json_body)
        

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()