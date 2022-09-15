
import BlynkLib
from BlynkTimer import BlynkTimer


# DHT11
import DHT11
dht11 = DHT11.DHT11(17)


def getTem():
    count = 0
    while True:
        result = dht11.get_result()
        count+=1
        if result:
            break
        if count>=100:
            return None
    temp=float(f"{result[2]}.{result[3]}")
    #print("Temperature: "+str(temp))
    return temp

# Blynk
BLYNK_AUTH = "337A0t0PWvZrzXFp4KWTKOMUm1BPdJng" #'YourAuthToken'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = BlynkTimer()


# Will only run once after 2 seconds
def hello_world():
    print("Start!")


# Will Print Every 10 Seconds
def publish_data():
    tempVal=getTem()
    blynk.virtual_write(5, tempVal)


# Add Timers
timer.set_timeout(2, hello_world)
timer.set_interval(10, publish_data)


while True:
    blynk.run()
    timer.run()