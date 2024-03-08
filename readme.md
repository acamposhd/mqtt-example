# Instructions

run pip install -r requirements.txt
to test locally uncomment
broker_address = "broker.hivemq.com" # dirección del broker
port=1883 #Puerto de conexión

and comment
broker_address = "http://0.tcp.us-cal-1.ngrok.io" # dirección del broker
port=17948 #Puerto de conexión

to test locally using docker, get into the docker folder and run docker-compose up -d

to test online we might change http://0.tcp.us-cal-1.ngrok.io to the current ngrok url provided
