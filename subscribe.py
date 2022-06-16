import random
from tkinter import TOP
import yaml
from paho.mqtt import client as mqtt_client
import pygame  
import morse_converter
from datetime import datetime
import time

with open("settings.yaml", 'r') as f:
    params = yaml.safe_load(f)


client_id = f"{params['client_id']}-{random.randint(0, 1000)}"
TOPIC = f"{params['topic']}/{params['publish_to']}"

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to MQTT Broker on topic {TOPIC}!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(params['username'], params['password'])
    client.on_connect = on_connect
    client.connect(params['broker'], params['port'])
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, data):
        msg: str = data.payload.decode()
        curr_time: str = datetime.now().strftime('%m%d%Y_%H%M%S')
        print(f"Received message from `{data.topic}` topic at " \
            f"{curr_time}")
        play_wav("sms.wav")
        input(f"Message has {len(msg)} characters. Are you ready to decode it?")
        morse_converter.msg_to_wav(msg, curr_time)
        time.sleep(1)
        play_wav(f"messages/{curr_time}.wav")
        input("Press enter to see the message in plaintext.")
        print(msg)
        
        
    client.subscribe(TOPIC)
    client.on_message = on_message

def play_wav(wav_path: str):
    pygame.mixer.init()
    pygame.mixer.music.load(wav_path)
    pygame.mixer.music.play()

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
