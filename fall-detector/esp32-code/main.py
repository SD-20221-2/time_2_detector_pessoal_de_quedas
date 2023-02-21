from time import sleep
from machine import Pin, SoftI2C, reset
from umqttsimple import MQTTClient
from urequests import get
from beep import n_normal_beeps

import mpu6050

global client_id, mqtt_server, port, user, password, keepalive, ssl, topic_pub

client_id = '0'
mqtt_server = 'af4a9c8ba3224e39aad654cebd6ac673.s2.eu.hivemq.cloud'
port = 8883
user = b'fall-detector'
password = b'fall-detector'
keepalive = 10
ssl = True
ssl_params={'server_hostname':'af4a9c8ba3224e39aad654cebd6ac673.s2.eu.hivemq.cloud'}
topic_pub = b'fall-detector-sd'

def connect():
    client = MQTTClient(client_id, mqtt_server, port, user, password, keepalive, ssl, ssl_params)
    client.connect()
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_pub))
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT Broker. Reconnecting...')
    sleep(10)
    reset()
    
def send_alert():
    try:
        client.publish(topic_pub, b'QUEDA DETECTADA!')
        print("Alert sent")
    except OSError as e:
        restart_and_reconnect()
    
try:
    client = connect()
except OSError as e:
    restart_and_reconnect()
    


# Initializes the I2C method for ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
# Starts the accelerometer
mpu = mpu6050.accel(i2c)

acceleration_counter = 0
stop_counter = 0

while True:
    sensor_values = mpu.get_values()
    accX = round( sensor_values["AcX"] / 1630 , 1 )
    accY = round( sensor_values["AcY"] / 1630 , 1 )
    accZ = round( sensor_values["AcZ"] / 1630 , 1 )
    print("Acceleration x-axis: " + str(accX) )
    print("Acceleration y-axis: " + str(accY) )
    print("Acceleration z-axis: " + str(accZ) )
    
    if abs(accX) > 20 or abs(accY) > 20 or abs(accZ) > 20:
        acceleration_counter += 1
        
    else:
        acceleration_counter = 0
    
    if acceleration_counter >= 15:
        n_normal_beeps(3)
        send_alert()
        acceleration_counter = 0
        sleep(10)
