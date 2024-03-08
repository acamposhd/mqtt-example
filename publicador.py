import pandas as pd
import paho.mqtt.client as mqttClient
import json
import time

dataframe = pd.read_csv('DatosPruebaMQTT.csv', index_col=0)
dataframe.head()
dataframe.describe(include="all")
df = dataframe.dropna()

temp = df.Temperature.tolist()
hum = df.Humidity.tolist()
co2 = df.CO2.tolist()

# Métodos de MQTT

def on_connect(client, userdata, flags, rc):

    if rc==0:
        print("Conectando al broker")
        global Connected
        Connected = True
    else:
        print("Falla en la conexión al broker")

# Esto debe ser cambiado por la dirección del broker    
broker_address = "http://0.tcp.us-cal-1.ngrok.io" # dirección del broker
port=17948 #Puerto de conexión



# Para correrlo localmente con 
# broker_address = "broker.hivemq.com" # dirección del broker
# port=1883 #Puerto de conexión

tagt = "TE4017/mqtt/equipo1/temperature"
tagh = "TE4017/mqtt/equipo1/humidity"
tagc = "TE4017/mqtt/equipo1/co2"

client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect 
client.connect(broker_address, port)
client.loop_start()

Connected = False

while Connected != True:
    time.sleep(0.5)
    try:
        for i,j,k in zip(temp,hum,co2):
            value1 = json.dumps({"Temperature":i})
            value2 = json.dumps({"Humidity":j})
            value3 = json.dumps({"CO2":k})
            print(tagt, value1,"\n", tagh, value2,"\n", tagc, value3)
            client.publish(tagt, value1)
            client.publish(tagh, value2)
            client.publish(tagc, value3)
    except KeyboardInterrupt: # Presionar Ctrl+C para salir
        print("Envio de datos detenido por el usuario")
        client.loop_stop()
        client.disconnect()
        break