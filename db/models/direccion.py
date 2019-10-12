import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()
    
from contacto import Contacto


class Direccion(models.Model):
    id: models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=250, default="")
    tipo = models.CharField(max_length=10, default="") ##principal or secundario
    estado = models.BooleanField(default=True)
    contacto = models.ForeignKey(Contacto,default=1, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "direcciones"