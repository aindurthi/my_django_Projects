# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Voter(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    DOB = models.DateField()
    def __str__(self):
        return self.first_name

class Choice(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    party = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.party