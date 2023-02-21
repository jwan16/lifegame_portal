from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from booth.models import BoothTraffic, Booth
from player.models import Player
# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return "{} - {} {}".format(self.id, self.last_name, self.first_name)

    def is_oc(self):
        print(self.user_type in ('oc', 'admin'))
        return self.user_type in ('oc', 'admin')

    def is_player(self):
        return Player.objects.filter(user=self).exists()

    def get_player(self):
        return Player.objects.filter(user=self).first()

    @property
    def player(self):
        return Player.objects.filter(user=self).first()

    user_type = models.CharField(
        max_length=10,
        choices=(('student', 'student'), ('oc', 'oc'),('admin', 'admin'), ('instructor', 'instructor')),
        blank=True, null=True
        )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True )
    school = models.CharField(max_length=100, blank=True, null=True)
    def get_last_seen(self):
        if self.is_player():
            last_seen = BoothTraffic.objects.filter(player=self.get_player()).order_by('-record_time').first()
            return last_seen
        return None