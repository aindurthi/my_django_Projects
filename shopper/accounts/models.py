from django.db import models
from django.utils.translation import ugettext_lazy as _

from authtools.models import AbstractNamedUser


class User(AbstractNamedUser):
    username = models.CharField(_('username'), max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    class Meta:
        db_table = 'auth_user'