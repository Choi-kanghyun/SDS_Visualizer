# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:24:10 2017

@author: kanghyun
"""

import sys
import requests, json

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



# URL Address -> 10.0.7.22 를 상황에 맞게 변형






############################################
#dataserver#
############################################
class dataServer:
    id = -1
    hostname = -1
    planeNo = -1
    tierNo = -1
    column = -1
    row = -1
    ip = -1
    URL_dataserver = 'http://10.0.7.22:8080/dataserver'
    res = requests.get(URL_dataserver)
   
    
    def getJsonOfDataServer(self):  # json 형식이 아닌, dict 형식으로 return 주의!
        return self.res.json()
    
    def getIdOfDataServer(self):
        temp = self.res.json()


    
###########################################
#dataserver state#
###########################################
class dataServerState:
    
    URL_dataserverstate = 'http://10.0.7.22:8080/dataserverstate'
    res = requests.get(URL_dataserverstate)
    
    def getJsonOfDataServerState(self):
        return self.res.json()
    

############################################
#cube#
############################################
class cube:
    
    URL_cube = 'http://10.0.7.22:8080/cube'
    res = requests.get(URL_cube)
    
    def getJsonOfCube(self):
        return self.res.json()
        
    
############################################
#disk#
############################################
class disk:
    
    URL_disk = 'http://10.0.7.22:8080/disk'
    res = requests.get(URL_disk)
    
    def getJsonOfDisk(self):
        return self.res.json()
    
############################################
        
    
        
#tmp = dataServer()
#dataserver_json=tmp.getJsonOfDataServer()
##print(dataserver_json)
#count = dataserver_json['count']

#for i in range(1, count):
#    print(dataserver_json['results'][i]['hostname'])
#else:
#    print('The for loop is over')
#    
#print(dataserver_json['results'][1]['hostname'])
#
#tmp2 = dataServerState()
##print(tmp2.getJsonOfDataServerState())
#
#tmp3 = cube()
##print(tmp3.getJsonOfCube())
#
#tmp4 = disk()
#print(tmp4.getJsonOfDisk())


##################test#######################
