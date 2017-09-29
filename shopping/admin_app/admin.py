# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Accessories)
admin.site.register(Tops)
admin.site.register(Bottoms)
admin.site.register(Outerwears)
admin.site.register(Footwears)

#admin.site.register(UserProfile)