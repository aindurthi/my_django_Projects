# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class login(models.Model):
    uname = models.CharField(max_length=30)
    psw = models.CharField(max_length=30)
    def __str__(self):
        return self.uname

class register(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone = models.IntegerField(max_length=10)
