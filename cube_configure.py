# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:24:10 2017

@author: kanghyun
"""
# bring to data in DB(dataserver) and start to initializing 

#from classes.getJson import *
import json


#tmp = dataServer()
# datas -> 미들웨어에서 받아온 DS 관련 데이터 값
#datas = tmp.getJsonOfDataServer()  # json 이 아닌 dict 형식으로 오는것에 주의!


#####################################################
# 원래라면 DataServer, Plane 등을 받아서 처리해야 하지만, 
# 아직 미들웨어부분 (특히 plane)이 작성되지 않았으므로,
# 1024DS , 4 Plane, 2 Tier 를 가정하여 큐브 작성 , 17.06.26
####################################################

vertices_list = []

class getLocate:    
    
    ds_x=0
    ds_y=0
    ds_z=0
    
    def locateDs(self, column, raw, tier, plane):  # 6.30 이부분 다시 함수로 완벽하게 구현, 지금은 임시로 1024일 경우만!
        
       #self.ds_z = ((tier*1))+((plane*2))  # 이걸 잘 수정해보자
       
       if tier == 0:
           self.ds_z = plane*2
           
       elif tier == 1:
           self.ds_z = ((plane*2)+1)
           
       self.ds_x = column
       self.ds_y = raw
    
    def getDs_x(self):
        return self.ds_x
    def getDs_y(self):
        return self.ds_y
    def getDs_z(self):
        return self.ds_z



def getVertices_list():
    return vertices_list


def setVertices_list(): # 전역변수 datas 를 통해, vertices_list 를 채운 후, 리턴하는 함
    locate = getLocate()
    #datas_result = datas['results']  #우선 임시 json 사용을 위해 주석 처리, '17.6.27
    open_json = open("temp_ds_json.json",'r')
    datas_result = json.load(open_json)
    
    for data in datas_result:
        locate.locateDs(data['column'], data['row'], data['tierNo'], data['planeNo'])
        x=locate.getDs_x()
        y=locate.getDs_y()
        z=locate.getDs_z()
        # vertices 값 만들기
        temp=((x,y,z),(x+1,y,z),(x+1,y+1,z),(x,y+1,z),
              (x,y,z+1),(x+1,y,z+1),(x+1,y+1,z+1),(x,y+1,z+1))
        
        vertices_list.append(temp)
        
    
    # print(vertices_list) 
    return vertices_list


    #17.6.27 , 이제 임시변수 만들어보자, 우선 논문 초록으로 진행 업무 변
    
