import json
from flask import Flask, jsonify
import sys

class Bot():
    app = Flask(__name__)

    def __init__(self, filename):
        self.dict = []
        self.fileame = filename

    def LoadSubSystems(self):
        f = open(self.fileame)        
        dataFile = json.load(f)
        for i in dataFile['SubSystem']:
            self.dict.append(i)
        f.close()
        return self.dict

    def CountLoadedSubSys(self):
        return len(self.dict)

    def getTempOfOneSS(self, num):
        for d in self.dict:
            if(d["id"] == num):
                return d["temp"]

    def GetMaxTemp(self):
        max = 0
        for d in self.dict:
            if(d["temp"] > max):
                max = d["temp"]
        return max

    def GetMinTemp(self):
        min = sys.maxsize
        for d in self.dict:
            if(d["temp"] < min):
                min = d["temp"]
        return min

    def getPWMs(self):
        PWM = []
        for i in self.dict:
            PWM.append(i["PWM"])
        return PWM

    def getPMWVariable(self):
        if(self.fileame == 'SubSystem_00.json'):
            return 0 #should be taken from Vaeiable
        if(self.fileame == 'SubSystem_01.json'):
            return 50        
        if(self.fileame == 'SubSystem_02.json'):
            return 99       
        if(self.fileame == 'SubSystem_03.json'):
            return 100

bub = Bot('SubSystem_Single_05.json')
print(bub.LoadSubSystems())
print(bub.GetMaxTemp())