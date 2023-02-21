from gc import collect
from ubinascii import hexlify
from umqttsimple import MQTTClient
from machine import unique_id
from wifi import do_connect

collect()

do_connect()
