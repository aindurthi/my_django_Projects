# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from colorful.fields import RGBColorField
#from colorfield.fields import ColorField

#INSTALLED_APPS.append('colorful')

GENDER = (
    ('men','MEN'),
    ('women','WOMEN'),
)

TOPS =(
    ('chanel','CHANl'),
    ('gucci','GUCCI'),
    ('prada','PRADA'),
    ('zara','ZARA'),
    ('bcbg','BCBG'),
)

CATEGORY = (
    ('tops','Tops'),
    ('bottoms',' Bottoms'),
    ('outerwear',' Outerwear'),
    ('footwear','Footwear'),
    ('accessories',' Accessories'),
)

SIZE = (
    ('s','S'),
    ('xs','XS'),
    ('m','M'),
    ('l','L'),
    ('xl','XL'),
    ('xxl','XXL'),
)

#def brand():
 #   if productdetails.category == 'Tops':
  #      return TOPS

class productdetails(models.Model):
    productname = models.CharField(max_length=40)
    gender = models.CharField(max_length=20, choices=GENDER)
    category = models.CharField(max_length=40, choices=CATEGORY)
    productcost = models.CharField(max_length=20,default='')
    productdescription =models.CharField(max_length=100,default='')
    productsize= models.CharField(max_length=5,choices=SIZE,default='')
    productcolor = RGBColorField(default='#FF0000')
   # productbrand = models.CharField(max_length=20,choices=brand())
    #def brand(self):
    #  if productdetails.category == 'Tops':
    #     topschoice = models.CharField(max_length=40,choices=TOPS)


    def __str__(self):
        return  self.productname

