'''
Created on Apr 3, 2011

@author: sah
'''
from google.appengine.ext.db import Model, UserProperty, DateTimeProperty, IntegerProperty, GeoPtProperty, StringProperty

class Knower(Model):
    account = UserProperty(auto_current_user=True)
    time = DateTimeProperty(auto_now=True)
    location = GeoPtProperty()
    credits = IntegerProperty(0)
    fines = IntegerProperty(0)
    pains = IntegerProperty(0)

class Knowledge(Model):
    account = UserProperty(auto_current_user=True)
    time = DateTimeProperty(auto_now=True)
    location = GeoPtProperty()
    info = StringProperty()
