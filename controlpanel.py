
"""
In The Name of God
@author: apm

ADV _ Project 1 

APM: ......


porozhe ee --> tozihat chie???
codesho bznim --> basic --> advanced

yeseri jahasho khali mizarim --> bayad oon ro por konid


deadline --> 2 hafte 

github --> chijori , project besazi, collaborator grhar




ADV _ PROJECT2
hal mishe
+ advanced --> ezafe mikonim
database, distribute, GUI (graphical user interface)
--> Market



#------------
1 --> Class Device (Reall) -0-> camera ba code 38
2--> PRINT( )--> print haro kamel konid
3-->yekseri tabe ye jadi man ezafe mikonm toosho khali 





"""





'''
IOT ---> internet of things
اینترنت اشیا


Device --> dastgah  (electronic device)

ina --> lamp , yakhchal , datsgah jaroo , dar , doorbin ,,....
kooler (fan) ,.... .khoone


device --> bargh beheshon ( AC , DC )
mostaghel daran kar mikonan va mano shoame ensan 
miaym inaro control mikonim

aya rahi has k ma btoonim haamshono ba ham kh awli control modiiat

yani too gooshit y barname bashe
k btooen b kole devcie haye khoant vasl she
va rahat btoni ghat koni vasl koni va ...

devcie --> beham vasl beshan (connect)
tamame --> control panel ( goshi , barname , )

control panel[] device electronic [otagh,klhoone, aparteman, vilaha]

karkhoonem sgherekate santi ,




--> IOT


inTERNET


madon ghermez
blu 


amvaje internet --> wifi , ...


interneti -->



#------------------
IOT---- [[[internet of things FINAL]]]
device ha [electronic] , interneti beham vasl she
be yek control panel vasl she k shoam modirat konid
#------------------





------THINGS-----------
1- Device --> chizi k shoma ono control modiriat, khamosh roshan
2- Sensor --> azacsh chizi daryaft mikoni , 
------------------------

rabtehs ba poython chie?

device --> motherboard ((element -> wifi ))

lampe mamooli--> elemnt toshe , bargh toosh va 
lamp haye hooshmand -> motherboard --> wifi vasl she
code 328732897623762



shoam behesh dastoor bedi ??


khoone [lamp] <------sherkat(ketabkhone) ----> python (khone)



API based --> Application programming interface



#------------

khoone (Computer --> OS --> IDE/EDITOR --> Python )
(computer --> OS --> Browser  --> getplutus.solutions )

request --> midi b in server????



server --> shekrata finanld , norway , aparatemean -->
ghafase --> case 
ejare mida


laptab , --> ip 
19.22.3223.3223


188.233.32332.323232



norway --> sakhtemon, laptab 23323.2332.232332.3232

dns --> domain 
getplutus.solutions --> 23323.2332.232332.3232




browser (laptab) --> getplutus.sopltuions --> browser
23323.2332.232332.3232 ip (laptabe man tooye norway)
request.
HTML pas mide

browser oon html (javascript, ..) render mikone namayesh mide



#------------


device besazim
1 device ??

1000 ta device


things --> 1-devcie 2-sensor

Type hast --> chanta azash bsazi

lamp1,lamp2,lkamp3 , door 1 , door2 ,.....

CLASS --> OBJECT MIKESHI BIROON


CLASS DEVICE MIKHAM

felan bai ye device besazim
badan 





'''




class Device:
    
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name




#a1= Device()

#location --> karaj , tehran , shiraz yazfd, ....
#group --> ashapzkhone, 

#lamps
#doors
#fans



#a1=Device('home','ashpazkhoone','lamps','lamps1')







class Device:
    
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name



a1=Device('home','room1','lamps','lamps1001')

#yek object az classs device
#inproperty haro dare

a1.location # 'home'
a1.group #
a1.device_type #'lamps'
a1.device_name #'lamps1001'

a1.turn_on()


a1.turn_off()





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


    def turn_off(self):
        print('off')
        self.status='off'
        
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        



a1=Device('home','ashpazkhoone','lamps','lamps707')


a1.device_name #'lamps707'

a1.status #'off'

a1.turn_on() #Done!!
a1.status #'on'


a1.turn_off() #off
a1.status #'off'


a1.get_status() # False


a1.turn_on() #Done!!!
a1.status # 'on'

a1.get_status() #True





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
        #oon devicer --> SHERKAT vasl bshe --> dastoopr bde --> sherkate b oon lampe vasl bshe
        #va oon lamp baram 'ROSHAN' kone


    def turn_off(self):
        print('off')
        self.status='off'
        #bayad inja bnvis-->sherkate begam agah in device 
        #shekrat elamp --> 'Khamoosh' kone
        
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
        
#-------------------------


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

    print(f'mqtt connected')
        
        
    def setup_gpio(self):
        
        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)
            
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)

elif self.device_type=='camera':
GPIO.setup(38,GPIO.OUT)

else:
    print(f'device type not defined')
            

    def turn_on(self):
        print(f'turn on',self.device_name)
        self.status='on'
        #oon devicer --> SHERKAT vasl bshe --> dastoopr bde --> sherkate b oon lampe vasl bshe
        #va oon lamp baram 'ROSHAN' kone
        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')
        
        

    def turn_off(self):
        print(f'turn off',self.device_name)
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

a1=Device('home','room','lights','lamps1001','w328376231863816326216','camera','camera1001')

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
            print(f'your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your device is added to {group_name}')
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
            print(f'your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your device is added to {group_name}')
        else:
            print(f'groups {group_name} is not exist....')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            
            self.groups[group_name].append(new_device)
            print(f'device','{device_name}' added to group '{group_name}'.')
            
        else:
            print(f'group','{group_name}' not found.') #...
        
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




#===================================
#-----****-----------
#--------TASK  2, 3-----------------
       

class Device:
    
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'


    def turn_on(self):
        print(f'device {self.device_name} in group {self.group} is ON')
        self.status='on'
        #--_.code ejra mishe

    def turn_off(self):
        print(f'device {self.dvice_name} in group {self.group} is OFF')
        self.status='off'
        #code ejra mishe 
       
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
        

class Sensor:
    
    def __init__(self,location,group,sensor_type,sensor_name):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
                
        
    def read_data(self):
       a=np.random.uniform(22,27)
       print(f'sensor {self.sensor_name} recorded {round(a,2)} c')
       return a




class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print(f'your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your device is added to {group_name}')
        else:
            print(f'group '{group_name}' not found.')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            
            self.groups[group_name].append(new_device)
            print(f'device{device_name} of type {device_type} created and added to group {group_name}.')
            
        else:
            print(f'group'{group_name}' was not found.')
        
        
        
        
    def create_multiple_device(self,group_name,device_type,device_number):
        if group_name in self.groups:
            
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)

            print(f'{device_number} devices created!!')
            
        else:
            
            print(f'group is not found')
            
            
            
    def get_devices(self,group_name):
        
        devices=self.groups[group_name]
        return devices
        
        
        
  def trun_on_in_group(self,group_name):

if group_name in self.groups:

devices=self.get_devices(group_name)

for device in devices:
device.turn_on()

else:
print('....')



def turn_off_in_group(self,group_name):
if group_name in self.groups:
    for device in
self.groups[group_name]:
    device.turn_off()
   print(f'all devices in {group_name} are off')
   else:
     print(f'group not found')




def turn_on_all(self):
   for group in self.groups:
      for device in self.groups[group]:
      device.turn_on()
print(f'all devices in home are on now')


def turn_off_all(self):
    for group in self.groups:
      for device in self.groups[group]:
         device.turn_off()
print(f'all devices in home are off now')



def get_status_in_group(self,group_name):
'''
be ezaye device haye tooye masalan felan group
living_room --> bebine roshanan ya khamoshan
porint kone

a.get_status_in_group('living_room')

device {name} is on
... .. .. ois off
.. .. .. is on
'''

def get_status_in_device_type(self,dvice_type):

'''
varaye kole devicd haee k hasan
bere device_typeshono check kone

fght lamparo bere check kone

lamps -->lampa
doors --L> fght doora
(too ch groupi , device_type)

statuseshono bede


'''
pass


#tabe ee bename create_device???

def create_sensor(self):
pass

def create_multiple_sensor(self):
pass






