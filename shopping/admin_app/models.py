#from __future__ import unicode_literals
from django.db import models
from colorful.fields import RGBColorField
from django.contrib.auth.models import User


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

ACCESSORIES = (
    ('mobiles','MOBILES'),
    ('jewel','JEWEL'),
    ('handbags','HANDBAGS'),
    ('watches','WATCHES'),
    ('handycraft','HANDYCRAFTS'),
    ('trimmers','TRIMMERS'),
)

FSIZE = ((5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12))

class Tops(models.Model):
    topname = models.CharField(max_length=20)
    topimage= models.ImageField()
    gender = models.CharField(max_length=20, choices=GENDER)
    topcost = models.CharField(max_length=20, default='')
    topdescription = models.CharField(max_length=100, default='')
    topsize = models.CharField(max_length=5, choices=SIZE, default='')
    topcolor = RGBColorField(default='#FF0000')
    topbrand = models.CharField(max_length=30, default='')
    def __str__(self):
        return self.topname

class Bottoms(models.Model):
    bottomname = models.CharField(max_length=20)
    bottomimage= models.ImageField()
    gender = models.CharField(max_length=20, choices=GENDER)
    bottomcost = models.CharField(max_length=20, default='')
    bottomdescription = models.CharField(max_length=100, default='')
    bottomsize = models.CharField(max_length=5, choices=SIZE, default='')
    bottomcolor = RGBColorField(default='#FF0000')
    bottombrand = models.CharField(max_length=30, default='')
    def __str__(self):
        return self.bottomname

class Outerwears(models.Model):
    outerwearname = models.CharField(max_length=20)
    outerwearimage= models.ImageField()
    gender = models.CharField(max_length=20, choices=GENDER)
    outerwearcost = models.CharField(max_length=20, default='')
    outerweardescription = models.CharField(max_length=100, default='')
    outerwearsize = models.CharField(max_length=5, choices=SIZE, default='')
    outerwearcolor = RGBColorField(default='#FF0000')
    outerwearbrand = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.outerwearname

class Footwears(models.Model):
    footwearname = models.CharField(max_length=20)
    footwearimage= models.ImageField()
    gender = models.CharField(max_length=20, choices=GENDER)
    footwearcost = models.CharField(max_length=20, default='')
    footweardescription = models.CharField(max_length=100, default='')
    footwearsize = models.CharField(max_length=5, choices=SIZE, default='')
    footwearcolor = RGBColorField(default='#FF0000')
    footwearbrand = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.footwearname
class Accessories(models.Model):
    accessoriesname = models.CharField(max_length=20)
    accessoriesimage= models.ImageField()
    gender = models.CharField(max_length=20, choices=GENDER)
    accessoriescost = models.CharField(max_length=20, default='')
    accessoriescategory= models.CharField(max_length=20,choices=ACCESSORIES)
    accessoriesdescription = models.CharField(max_length=100, default='')
    accessoriessize = models.CharField(max_length=5, choices=SIZE, default='')
    accessoriescolor = RGBColorField(default='#FF0000')
    accessoriesbrand = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.accessoriesname

'''class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username'''

#from django.contrib.auth.models import User
#from .forms import SignUpForm
from django import forms
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length=30, required=True)
    first_name = models.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = models.CharField(max_length=30, required=False, help_text='Optional.')
    email = models.CharField(max_length=254)
    password = models.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = models.CharField(widget=forms.PasswordInput())

    def __str__(self):
        return  self.username

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


#class User(AbstractUser,Per):
#   username = None
    email = models.EmailField(_('email address'), unique=True)
