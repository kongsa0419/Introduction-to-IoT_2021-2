import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid):
    print("on_publish called")
    mqttc.disconnect()

mqttc = mqtt.Client()
mqttc.on_publish = on_publish

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
#mqttc.connect("192.168.0.3")
mqttc.connect("localhost")

mqttc.loop_start()

mqttc.publish("hello/world", "Hello")

mqttc.loop_stop()
