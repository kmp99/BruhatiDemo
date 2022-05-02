# import urllib library
from urllib.request import urlopen

# import json
import json

#import mqtt library
import paho.mqtt.client as mqtt

# store the URL in url as
# parameter for urlopen
url = "http://172.16.10.22/fx9600/bancali_imp"


# store the response of URL
#response = urlopen(url)

# storing the JSON response
# from url in data
#data_json = json.loads(response.read())

# print the json response


#connect to the brocker

Broker = "mqtt://bruhati.eu-latest.cumulocity.com"
port = 1883

client = mqtt.Client()
try:
	client.connect(Broker,port)
except:
	print("Device is offline/Endpoint not found")
	exit()



#topic is created by the server, just created for testing
topic = "topic/test"

#Defin MQTT Message
mqttMessage = {}


try:
    while True:
		response = urlopen(url)
        data_json = json.loads(response.read())
        print(data_json)
        data = data_json
        if (data) :
			#ID
            mqttMessage.id = data.mac_address
            #Name
            mqttMessage.name = data.reader_name
            #Tag_Read
            mqttMessage.jsonData = data.tag_reads
			client.publish(topic,data)
			print("")
			print("Published data to MQTT: bruhati.eu-latest.cumulocity.com")
			print("")
			print("")
		else:
			print("Data not found")
        time.sleep(15)
##
except TypeError:
       print ("type error")
except KeyboardInterrupt:
       print ("IO Error")
