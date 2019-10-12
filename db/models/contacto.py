# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 09:39:55 2019

@author: E201
"""
import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()
    
# Sample User model
class Contacto(models.Model):
    id: models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, default="")
    fecha_nacimiento = models.DateField()
    DNI = models.CharField(max_length=45, default="")
    tipo_DNI = models.CharField(max_length=45, default="")
    municipio = models.IntegerField(max_length=45, default="")
    pais = models.IntegerField(max_length=45, default="")
    estado = models.BooleanField()

    class Meta:
        db_table = "contactos"

    def __str__(self):
        return self.nombre

    __repr__ = __str__

