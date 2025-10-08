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
            

    def turn_on(self):
        print('Done!!!')
        self.status='on'
        #oon devicer --> SHERKAT vasl bshe --> dastoopr bde --> sherkate b oon lampe vasl bshe
        #va oon lamp baram 'ROSHAN' kone
        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')
        
        

    def turn_off(self):
        print('off')
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

a1=Device('home','room','lights','lamps1001','w328376231863816326216')

a1.turn_on()

a1.turn_off()



class Sensor:
    
    def __init__(self,location,group,sensor_name,sensor_type,pin):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
        
        self.pin=pin
        
        
a1=Sensor('hom','room1','temp','thermoset10','2823shasjash')


a1.location

a1.pin


#a1.turn_on()

#**things -_> device / sensor
#devcie -->dastoor turn on , off


#sensor--> damaor , begiri data -->: read_data()


    
import Adafruiy_DHT   
    
class Sensor:
    
    def __init__(self,location,group,sensor_name,sensor_type,pin):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
        
        self.pin=pin
        
        
    def read_data(self):
        humidity,temeprature=Adafruiy_DHT.read_retry(Adafruiy_DHT.DHT22,self.pin)
        
        return temeprature
        
a1=Sensor('hom','room1','temp','thermoset10','2823shasjash')


a1.read_data()      
        









'''


PROJECT 1 


ghesmate 1 -----------------
lights, doors --> camera ro poshesh 

class device be goone e ke camra ro ham support
code camera --> 38   lahaaz



ghesmate 2 -----------------------



'''


#-------------> device , pin 

class Device:
    
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'


    def turn_on(self):
        print('Done!!!')
        self.status='on'
        #--_.code ejra mishe

    def turn_off(self):
        print('off')
        self.status='off'
        #code ejra mishe 
       
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
    
#---> TOO KHONE 
a1=Device('home','room','lights','lamps1')
a2=Device('home','room','lights','lamps2')
a2=Device('home','room','lights','lamps2')

a2=Device('home','room','lights','lamps2')

a2=Device('home','room','lights','lamps2')

a2=Device('home','room','lights','lamps2')

a2=Device('home','room','lights','lamps2')

a2=Device('home','room','lights','lamps2')

a2=Device('home','room','lights','lamps2')

a2=Device('home','room','lights','lamps2')

#/....
#for ????



#6 tasho posht kahmosh
#roshan konm


#ye devic jadid

#device otaghe 3 

#otaghe 4 o roshan konm



    
    
    
import numpy as np


class Sensor:
    
    def __init__(self,location,group,sensor_type,sensor_name):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
                
        
    def read_data(self):
        a=np.random.uniform(22,27)
        # b=int(a)
        return a
        #return b
       #return 25




a1=Sensor('home', 'room', 'thermo', 'thermo1001')

a1.location
a1.sensor_type
a1.sensor_name


a1.read_data() # 25.562291092722145

a1.read_data() #23.697334308191728

a1.read_data()
 


#----------------------------


'''

dictionary --> {}

groups 


group??- --> oon jaye daghigeh otagh, wc , parking ,pazirae 

groups --> jam egrouop




'''


class control_panle:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        self.groups[group_name]=[]
        print(f'groups {group_name} created !!')
        
        
        
a=control_panle()
        
a.groups #{}

'''


keys     Values

id      32923
name    233




dict groups

living_room  : []


wc  : []

parkign : []

room1 : []

'''

a.create_group('living_room')

#groups living_room created !!

a.groups

# {'living_room': []}





class control_panle:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
        
        
   
'''
dict groups

living_room  : []

wc  : []

parkign : []

room1 : []







ba in create_group --> liste khali
room1 room2 rookm3 living__rom , main_hull , oarking ,.....

[] listi az device haaa




groups


dict groups

living_room  : [device1 , device 2 , device3 , device4]

wc  : [device 10 ,.devcie 11 , devcie 13]

parkign : []

room1 : []




'''
        
       
        
class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
a= control_panel()   

a.create_group('living_room')  
        
a.create_group('parking')

a.groups

'''
{'living_room': [],
 
 'parking': []}

'''

#a.add_device_to_group(group_name,device1)


class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your devic is added to {group_name}')
        else:
            print('you group is not exist....')
        
        
a=control_panel()
  

a.groups #Out[46]: {}

a.create_group('living_room')
#groups living_room created !!
a.create_group('paerking')


a.groups
#{'living_room': []}


my_device=Device('home','living_room','lamps','lamps1001')
a.add_device_to_group('living_room', my_device)

#your devic is added to living_room

a.groups


'''
Out[52]: {'living_room': [<__main__.Device at 0x30d408730>]}


'''

mygp=a.groups

lv_room=mygp['living_room']

print(lv_room)
#[<__main__.Device object at 0x30d408730>]

mydv=lv_room[0]

mydv.location # 'home'
mydv.device_type
mydv.device_name #'lamps1001'


mydv.turn_on()

mydv.turn_off()


print(a.groups)

'''
{'living_room': [device1,devcie2,device3], 
 'paerking': []}




device1--> name.location, type , turn_on, turnOff

'''





class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your devic is added to {group_name}')
        else:
            print('you group is not exist....')
        
        
        
     
        
     
        
class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your devic is added to {group_name}')
        else:
            print('you group is not exist....')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            
            self.groups[group_name].append(new_device)
            print('///////bamofghtia')
            
        else:
            print('agha in esm vojod ndre') #...
        
a=control_panel()     
        
        
a.groups     #{}

a.create_group('living_room')   
        
a.groups
'''
Out[68]: {'living_room': []}

'''


#device --> lamps 1 --> living room

#rahe aval-->
mydv=Device('home','living_room','lamps','lamps1001') 
a.add_device_to_group('living_room', mydv)


#rahe dovom
a.create_device('living_room', 'lamps', 'lamps2001')

a.create_device('living_room', 'lamps', 'lamps328367')

a.create_device('living_room', 'lamps', 'lamps38123776')


       
a.groups

'''

{'living_room': [<__main__.Device at 0x30d40b9d0>,
  <__main__.Device at 0x30d40be20>,
  <__main__.Device at 0x30d4087f0>]}






{'living_room': [device1,device2,device13]}




'''



       
class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your devic is added to {group_name}')
        else:
            print('you group is not exist....')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            
            self.groups[group_name].append(new_device)
            print('///////bamofghtia')
            
        else:
            print('agha in esm vojod ndre') #...
        
        
        
        
    def create_multiple_device(self,group_name,device_type,device_number):
        if group_name in self.groups:
            
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)

            print(f'{device_number} devices created!!')
            
        else:
            
            print('....')
        
       
a=control_panel()     
        
        
a.groups     #{}

a.create_group('living_room')   


a.create_multiple_device('living_room', 'lamps', 40)



a.groups

'''
{'living_room': [<__main__.Device at 0x30d4db1f0>,
  <__main__.Device at 0x30d4d9240>,
  <__main__.Device at 0x30d4db5b0>,
  <__main__.Device at 0x30d4db580>,
  <__main__.Device at 0x30d4db4c0>,
  <__main__.Device at 0x30d4db4f0>,
  <__main__.Device at 0x30d4db5e0>,
  <__main__.Device at 0x30d4db610>,
  <__main__.Device at 0x30d4db700>,
  <__main__.Device at 0x30d4db730>,
  <__main__.Device at 0x30d4db640>,
  <__main__.Device at 0x30d4db3d0>,
  <__main__.Device at 0x30d4db3a0>,
  <__main__.Device at 0x30d4db2b0>,
  <__main__.Device at 0x30d4db310>,
  <__main__.Device at 0x30d4dae90>,
  <__main__.Device at 0x30d4d9f60>,
  <__main__.Device at 0x30d4d9f30>,
  <__main__.Device at 0x30d4dada0>,
  <__main__.Device at 0x30d4dad70>,
  <__main__.Device at 0x30d4da830>,
  <__main__.Device at 0x30d4d8bb0>,
  <__main__.Device at 0x30d4d8eb0>,
  <__main__.Device at 0x30d4da860>,
  <__main__.Device at 0x30d4d8fd0>,
  <__main__.Device at 0x30d4d9000>,
  <__main__.Device at 0x30d4d8ee0>,
  <__main__.Device at 0x30d4d8c10>,
  <__main__.Device at 0x30d4d8c40>,
  <__main__.Device at 0x30d4d8640>,
  <__main__.Device at 0x30d4d8e20>,
  <__main__.Device at 0x30d4dae00>,
  <__main__.Device at 0x30d4dae30>,
  <__main__.Device at 0x30d4daf50>,
  <__main__.Device at 0x30d4daef0>,
  <__main__.Device at 0x30d4d8790>,
  <__main__.Device at 0x30d4d83d0>,
  <__main__.Device at 0x30d4d9180>,
  <__main__.Device at 0x30d4d91b0>,
  <__main__.Device at 0x30d4d8280>]}



{'living_room' : [device1, devcie2 , ..... ,devcie3] }

'''



mygp=a.groups


lv_room=mygp['living_room']


dv1=lv_room[0]

print(type(dv1)) #<class '__main__.Device'>

dv1.device_type #'lamps'
dv1.device_name # 'lamps_1'

dv1.turn_on()


dv1.get_status() # True



dv10=lv_room[9]
dv10.device_name  # 'lamps_10'
dv10.get_status() #False

dv10.turn_on()

dv10.get_status() # True




'''


{ 'living_room' : [dv1,dv2,dv3,dv4]}


devices=[dv1,dv2,dv3,dv4]


for device in devices


device=dv1
device=dv2
device=dv3



'''




