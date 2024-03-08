import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Conectando al broker")
        global Connected
        Connected = True
    else:
        print("Falla en la conexión al broker")

def on_message(client, userdata, message):
    print(f"Mensaje recibido - {message.topic}:{message.payload.decode('utf-8')}")

# Esto debe ser cambiado por la dirección del broker
broker_address = "http://0.tcp.us-cal-1.ngrok.io" # dirección del broker
port=17948 #Puerto de conexión

# Para correrlo localmente con 
# broker_address = "broker.hivemq.com" # dirección del broker
# port=1883 #Puerto de conexión

tag = "TE4017/mqtt/equipo1/#"

client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)
client.loop_start()

Connected = False

while Connected != True:
    time.sleep(0.5)
    try:
        while True:
            time.sleep(1)
            client.subscribe(tag)
    except KeyboardInterrupt: # Presionar Ctrl+C para salir
        print("Envio de datos detenido por el usuario")
        client.loop_stop()
        client.disconnect()
        break
