# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 09:40:32 2019

@author: E201
"""

import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()
    
from contacto import Contacto

# Sample Role model

class Email(models.Model):
    id: models.AutoField(primary_key=True)
    correo = models.CharField(max_length=45, default="")
    tipo = models.CharField(max_length=10, default="") ##principal or secundario
    estado = models.CharField(max_length=10, default="")
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "emails"