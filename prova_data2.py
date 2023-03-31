# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:49:17 2023

@author: marku
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import data
datos1=[]
datos2=[]
datos3=[]
file=open('Tamb_totes.txt','r')
contenido=file.readlines()
for i in range (3,len(contenido),1): 
   dato1=contenido[i].find('\t')
   dato2=contenido[i].find('\t',dato1+1)
   dato3=contenido[i].find('\t',dato2+1)

#he canviat aquesta frase
#no entec res
   
