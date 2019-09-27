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

class resultados(Fact):
    pass


class SoilAnalyze(KnowledgeEngine):
    @Rule(Component(ph=P(lambda ph:ph>=7.2)))
    def isAlkaline(self):        
        print("\n \n \n")
        print("==> ph: ALCALINO")
        self.declare(Component (PH='ALCALINO'))
        

    @Rule(Component(ph=P(lambda ph:ph>6.8)&P(lambda ph:ph<=7.2)))
    def slightlyAlkaline(self):
        self.declare(Component (PH='LIGERAMENTE ALCALINO'))
        print("\n \n \n")
        print("==> ph: LIGERAMENTE ALCALINO")      
        self.declare(Component (PH='LIGERAMENTE ALCALINO'))
        

    @Rule(Component(ph=P(lambda ph:ph<=6.8)&P(lambda ph:ph>=6.2)))
    def Neutral(self):
        print("\n \n \n")
        print("==> Ph: NEUTRO")
        self.declare(Component (PH='NEUTRO'))
        
    @Rule(Component(ph=P(lambda ph:ph>5.6)&P(lambda ph:ph<6.2)))
    def slightlyAcid(self):
        print("\n \n \n")
        print("==> Ph: LIGERAMENTE ACIDO")
        self.declare(Component (PH='LIGERAMENTE ACIDO'))
    
    @Rule(Component(ph=P(lambda ph:ph<5.6)))
    def Acid(self):
        print("\n \n \n")
        print("==> Ph:  ACIDO")
        self.declare(Component (PH='ACIDO'))
    @Rule(Component(ce=P(lambda ce:ce<0.8)))
    def LowCE(self):
        print("\n \n \n")
        print("==> Conductividad electrica: BAJA")
        self.declare(Component (CE='BAJA'))
        
    @Rule(Component(ce=P(lambda ce:ce>=0.8)))
    def HighCE(self):
        print("\n \n \n")
        print("==>Conductividad electrica: ALTA")
        self.declare(Component (CE='ALTA'))
    
    @Rule(Component(PH=P(lambda PH: PH=='ALCALINO')))
    def extractAlkaline(self):
        print("\n \n \n")
        print("==> Extracto solubLe= TRUE")
        
    @Rule(Component(PH=P(lambda PH: PH=='LIGERAMENTE ALCALINO')))
    def extractAlkaline(self):
        print("\n \n \n")
        print("==> Extracto solubLe= TRUE")
        
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0)) & Component(PH=P(lambda PH:PH=='ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule9(self):
        print("\n \n \n")
        print("|-(1) Limitaciones de movimiento de agua")
        print("|-(2) Baja difusion de Oxigeno y flujo de gases")
        print("|-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("|-(4) Acumulacion de iones alcalinoterreos")
        
    @Rule(Component(arena=P(lambda arena:arena>=50.0)) & Component(PH=P(lambda PH:PH=='ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule10(self):
        print("\n \n \n")
        print("|-(1) Limitaciones de movimiento de agua")    
    
    @Rule(Component(limo=P(lambda limo:limo>=45.0)) & Component(PH=P(lambda PH:PH=='ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule11(self):
        print("\n \n \n")
        print("|-(1) Coloraciones grises suelo (Glaizeado)") 
        print("|-(2) Suelo Hidromorfico")
        print("|-(3) Limitaciones fisicas temporales")
        print("|-(4) Baja difusion de Oxigeno y flujo de gases")
        
    @Rule(Component(limo=P(lambda limo:limo<=40.0)) & Component(arena=P(lambda arena:arena<=40.0))& Component(arcilla=P(lambda arcilla:arcilla<=40.0))& Component(PH=P(lambda PH:PH=='ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule12(self):
        print("\n \n \n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
    
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))&Component(PH=P(lambda PH:PH=='ALCALINO'))&Component(CE=P(lambda CE:CE=='BAJA')))
    def rul13(self):
        print("\n \n \n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos")
        print("     |-(5) Baja disponibilidad de elementos menores")
    
    @Rule(Component(arena=P(lambda arena:arena>=50.0)) & Component(PH=P(lambda PH:PH=='ALCALINO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule14(self):
        print("\n \n \n")
        print("     |-(1) Revisar las mediciones realizadas.")
        
    @Rule(Component(limo=P(lambda limo:limo>=45.0))& Component(PH=P(lambda PH:PH=='ALCALINO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule15(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")
    @Rule(Component(limo=P(lambda limo:limo<=40.0))& Component(PH=P(lambda PH:PH=='ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule16(self):
        print("\n \n \n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule17(self):
        print("\n \n \n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")
    
    @Rule(Component(arena=P(lambda arena:arena>=50.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule18(self):
        print("\n \n \n")
        print("     |-(1) Revisar las mediciones realizadas.")
    
    @Rule(Component(limo=P(lambda limo:limo>=45.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule19(self):
        print("\n \n \n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
     
    @Rule(Component(limo=P(lambda limo:limo<=40.0))&Component(arena=P(lambda arena:arena<=40.0))&Component(arcilla=P(lambda arcilla:arcilla<=40.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule20(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ALCALINO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule21(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")
    
    @Rule(Component(arena=P(lambda arena:arena>=50.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ALCALINO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule22(self):
        print("\n \n \n")
        print("     |-(1) Revisar las mediciones realizadas.")
    
    @Rule(Component(limo=P(lambda limo:limo>=45.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ALCALINO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule23(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ") 

    @Rule(Component(limo=P(lambda limo:limo<=40.0))& Component(arcilla=P(lambda arcilla:arcilla<=40.0))& Component(arena=P(lambda arena:arena<=40.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ALCALINO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule24(self):
        print("\n \n \n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")
        
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))& Component(PH=P(lambda PH:PH=='NEUTRO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule25(self):
        print("\n\n\n")
        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Salinidad en el suelo")
        
    @Rule(Component(arena=P(lambda arena:arena>=50.0))& Component(PH=P(lambda PH:PH=='NEUTRO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule26(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
    
    @Rule(Component(limo=P(lambda limo:limo>=45.0))& Component(PH=P(lambda PH:PH=='NEUTRO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule27(self):
        print("\n \n \n")
        print("     |-(1) Salinidad en el suelo")
    
    @Rule(Component(limo=P(lambda limo:limo<=40.0))&Component(arena=P(lambda arena:arena<=40.0))&Component(arcilla=P(lambda arcilla:arcilla<=40.0))& Component(PH=P(lambda PH:PH=='NEUTRO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule28(self):
        print("\n\n\n")
    
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))& Component(PH=P(lambda PH:PH=='NEUTRO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule29(self):
        print("\n \n \n")
        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Limitaciones de movimiento de agua")
        
    @Rule(Component(arena=P(lambda arena:arena>=50.0))& Component(PH=P(lambda PH:PH=='NEUTRO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule30(self):
        print("\n \n \n")
        print("     |-(1) Revisar las mediciones realizadas.")
        
    @Rule(Component(limo=P(lambda limo:limo>=45.0))& Component(PH=P(lambda PH:PH=='NEUTRO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule31(self):
        print("\n \n \n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        
    @Rule(Component(limo=P(lambda limo:limo<=40.0))&Component(arena=P(lambda arena:arena<=40.0))&Component(arcilla=P(lambda arcilla:arcilla<=40.0))& Component(PH=P(lambda PH:PH=='NEUTRO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule32(self):
        print("\n \n \n")

    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule33(self):
        print("\n \n \n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")
    
    @Rule(Component(arena=P(lambda arena:arena>=50.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule34(self):
        print("\n \n \n")
        print("     |-(1) Revisar las mediciones realizadas.")
        
    @Rule(Component(limo=P(lambda limo:limo>=45.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule35(self):
        print("\n \n \n")
        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")
    
    @Rule(Component(limo=P(lambda limo:limo<=40.0))&Component(arena=P(lambda arena:arena<=40.0))&Component(arcilla=P(lambda arcilla:arcilla<=40.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule36(self):
        print("\n \n \n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ACIDO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule37(self):
        print("\n \n \n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")
        
    @Rule(Component(arena=P(lambda arena:arena>=50.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ACIDO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule38(self):
        print("\n \n \n")
        print("     |-(1) Revisar las mediciones realizadas.")
        
    @Rule(Component(limo=P(lambda limo:limo>=45.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ACIDO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule39(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")
    @Rule(Component(limo=P(lambda limo:limo<=40.0))&Component(arena=P(lambda arena:arena<=40.0))&Component(arcilla=P(lambda arcilla:arcilla<=40.0))& Component(PH=P(lambda PH:PH=='LIGERAMENTE ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule40(self):
        print("\n \n \n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))& Component(PH=P(lambda PH:PH=='ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule41(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Acumulacion de iones alcalinoterreos	")
        print("     |-(4) Salinidad en el suelo")
        print("     |-(5) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(6) Baja disponibilidad de Calcio")
        print("     |-(7) Contenido de Aluminio")
        
    @Rule(Component(arena=P(lambda arena:arena>=50.0))& Component(PH=P(lambda PH:PH=='ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule42(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
  
    @Rule(Component(limo=P(lambda limo:limo>=45.0))& Component(PH=P(lambda PH:PH=='ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule43(self):
        print("\n\n\n")
        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")
        
    @Rule(Component(limo=P(lambda limo:limo<=40.0))&Component(arena=P(lambda arena:arena<=40.0))&Component(arcilla=P(lambda arcilla:arcilla<=40.0))& Component(PH=P(lambda PH:PH=='ACIDO'))& Component(CE=P(lambda CE:CE=='ALTA')))
    def rule44(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
    
    @Rule(Component(arcilla=P(lambda arcilla:arcilla>=40.0))& Component(PH=P(lambda PH:PH=='ACIDO'))& Component(CE=P(lambda CE:CE=='BAJA')))
    def rule41(self):
        print("\n\n\n")    
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")
        
        
#-------------TEST--------------    
analisis = SoilAnalyze()
analisis.reset()
analisis.declare(Component(limo=20,arena=20,arcilla=60,ph=3,ce=0.2))
analisis.run()