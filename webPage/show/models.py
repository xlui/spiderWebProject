from django.db import models
from mongoengine import *
connect('xiaozhu')

class Information(Document):
    _id = StringField()
    title = StringField()
    address = StringField()
    price = StringField()
    img = StringField()
    hostPic = StringField()
    hostName = StringField()
    hostGender = StringField()

    meta = {'collection': 'Info_new'}

print(Information.objects.count())