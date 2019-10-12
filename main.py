# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:22:41 2019

@author: E201
"""

    
# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

# Import your models for use in your script
from db.models import User, Role

print('Truncating users...')
count_user = User.objects.all().count()
print('Count User before truncate: ', count_user)
#Truncate table User
User.objects.all().delete()
count_user = User.objects.all().count()
print('Count User after truncate: ', count_user)

print('Truncating roles...')
#Truncate table Roles
count_role = Role.objects.all().count()
print('Count Role before truncate: ', count_role)
Role.objects.all().delete()
count_role = Role.objects.all().count()
print('Count Role before truncate: ', count_role)

#Create Roles
role_admin = Role()
role_admin.name = 'Admin'
role_admin.status='Active'
role_admin.save()

role_client = Role()
role_client.name = 'Client'
role_client.status='Active'
role_client.save()

role_worker = Role()
role_worker.name = 'Worker'
role_worker.status='Active'
role_worker.save()

role_fake = Role()
role_fake.name = 'Fake'
role_fake.status='Inactive'
role_fake.save()

#Create User
user = User()
user.name = 'Jhon'
user.last_name='Murillo'
user.email='jhon@gmail.com'
user.id_role=role_admin
user.save()

user2 = User()
user2.name = 'Jhon2'
user2.id_role=role_client
user2.save()

user5 = User()
user5.name = 'Alex'
user5.last_name='Osorio'
user5.email='aosorio@gmail.com'
user5.id_role=role_worker
user5.save()

user3 = User()
user3.name = 'Fake1'
user3.last_name='Fake1'
user3.email='Fake1@gmail.com'
user3.id_role=role_worker
user3.save()

user4 = User()
user4.name = 'Fake2'
user4.last_name='Fake2'
user4.email='Fake2@gmail.com'
user4.id_role=role_worker
user4.save()

#Get All User
print('After Create')
for u in User.objects.all():
	print("ID: " + str(u.id) + "\tName: " + u.name + "\tLast Name: " + u.last_name, "\tEmail: " + u.email, "\tRole: " + str(u.id_role))

#Get By Param User    
user_edit = User.objects.get(name='Jhon2')
#Update User 
user_edit.last_name='Cordoba'
user_edit.email='jhonCordoba@gmail.com'
user_edit.save()

print('After Update')
for u in User.objects.all():
	print("ID: " + str(u.id) + "\tName: " + u.name + "\tLast Name: " + u.last_name, "\tEmail: " + u.email, "\tRole: " + str(u.id_role))

#Delete by filter
User.objects.filter(name='Fake1').delete()

#Delete by instance
user_delete = User.objects.get(name='Fake2')
user_delete.delete()

print('After Delete')
for u in User.objects.all():
	print("ID: " + str(u.id) + "\tName: " + u.name + "\tLast Name: " + u.last_name, "\tEmail: " + u.email, "\tRole: " + str(u.id_role))
