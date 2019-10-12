# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:11:59 2019

@author: E201
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pruebadbj',
        'USER': 'julio',
        'PASSWORD': 'estudiante',
        'HOST': '10.10.141.33',
        'PORT': '3306',
    }
}
        
INSTALLED_APPS = (
    'db',
)

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = '6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa'