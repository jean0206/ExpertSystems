# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 00:56:07 2019

@author: jeank
"""

#Comentario
from random import choice
from pyknow import *

class Component(Fact):
    """Info about the traffic light."""
    pass


class RobotCrossStreet(KnowledgeEngine):
    @Rule(Component(ph=P(lambda ph:ph>=7.2)),NOT(Component(PH=W())))
    def isAlkaline(self):        
        print("ph: ALCALINO")
        Component(PH=L('ALCALINO'))
        

    @Rule(Component(ph=P(lambda ph:ph>6.8)&P(lambda ph:ph<=7.2)))
    def slightlyAlkaline(self):
        print("ph: LIGERAMENTE ALCALINO")

    @Rule(Component(ph=P(lambda ph:ph<=6.8)&P(lambda ph:ph>=6.2)))
    def Neutral(self):
        
        print("Ph: NEUTRO")
        
    @Rule(Component(ph=P(lambda ph:ph>5.6)&P(lambda ph:ph<6.2)))
    def slightlyAcid(self):
        
        print("Ph: LIGERAMENTE ACIDO")
    
    @Rule(Component(ph=P(lambda ph:ph<5.6)))
    def Acid(self):
        print("Ph:  ACIDO")
        
    @Rule(Component(CE=P(lambda CE:CE<0.8)))
    def LowCE(self):
        print("Conductividad electricas: BAJA")
    
    @Rule(Component(CE=P(lambda CE:CE>=0.8)))
    def HighCE(self):
        print("Conductividad electricas: ALTA")
    
    @Rule(AS.PH<<Component(PH=L('ALCALINO')))
    def extractAlkaline(self):
        print("Extracto solubre= TRUE")
   
        

engine = RobotCrossStreet()
engine.reset()
engine.declare(Component(ph=8,CE=0.9))
engine.run()