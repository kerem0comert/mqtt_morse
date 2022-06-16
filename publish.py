import random
import time
from paho.mqtt import client as mqtt_client
import yaml
import argparse
import morse_converter
import pygame

with open("settings.yaml", 'r') as f:
    params = yaml.safe_load(f)


client_id = f"{params['client_id']}-{random.randint(0, 1000)}"
TOPIC = f"{params['topic']}/{params['publish_to']}"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            client.connected_flag = True
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.connected_flag = False
    client.username_pw_set(params['username'], params['password'])
    client.on_connect = on_connect
    client.connect(params['broker'], params['port'])
    return client


def single_publish(client: mqtt_client.Client, msg: str) -> None:
    parse_result(client.publish(TOPIC, msg)[0], msg)

def loop_publish(client: mqtt_client.Client) -> None:
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        parse_result(client.publish(TOPIC, msg)[0], msg)
        msg_count += 1


def parse_result(result: int, msg: str):
    # result: [0, 1]
    if result == 0:
        print(f"Send {msg} to topic {TOPIC}")
    else:
        print(f"Failed to send message to topic {TOPIC}")


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--msg', help='Message to publish', required=True)
    args = vars(parser.parse_args())
    if args['msg']:
        client: mqtt_client.Client  = connect_mqtt()
        client.loop_start()
        while not client.connected_flag:
            print("Waiting to connect...")
            time.sleep(0.5)
        single_publish(client, morse_converter.morse_to_plaintext(args['msg']))

if __name__ == '__main__':
    run()
