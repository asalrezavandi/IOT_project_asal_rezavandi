#**************************************************
#=========== DEVICE ASLIE 1001 =======================

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO  



class Device:
    
    def __init__(self,location,group,device_type,device_name,pin):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'
        
        
        #sherkat dade beman
        self.mqtt_broker='jasdhash'
        self.port=37362  
        
        #on dastgahe pini --> 
        self.mqtt_client=pin
        
        self.connect_mqtt()
        self.setup_gpio()
        



    def connect_mqtt(self):
        mqtt.connect(self.mqtt_broker,self.port)
        
        
    def setup_gpio(self):
        
        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)
            
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)

            elif self.device_type=='camera':
                GPIO.setup(38,GPIO.OUT)

else:
print('decive type not defined'):
            

    def turn_on(self):
        print('turn on',self.device_name)
        self.status='on'
        #oon devicer --> SHERKAT vasl bshe --> dastoopr bde --> sherkate b oon lampe vasl bshe
        #va oon lamp baram 'ROSHAN' kone

        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')
        
        

    def turn_off(self):
        print('turn off',self.device_name)
        self.status='off'
        #bayad inja bnvis-->sherkate begam agah in device 
        #shekrat elamp --> 'Khamoosh' kone
        mqtt.publish(self.mqtt_client,self.device_name,'TURN OFF')

        
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
#a1=..... (class --> device az tarighe ketabkhone)

a1=Device('home','room1','lights','camera','camera1001',38 )

a1.turn_on()

a1.turn_off()

