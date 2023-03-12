from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from booth.models import BoothTraffic, Booth
from player.models import Player
from django.utils.crypto import get_random_string
# Create your models here.

class User(AbstractUser):
    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{}{} - {} {}".format('{:03d}'.format(self.id), self.school_code, self.last_name, self.first_name)

    def is_oc(self):
        return self.user_type in ('oc', 'admin')

    def is_player(self):
        return Player.objects.filter(user=self).exists()

    def get_player(self):
        return Player.objects.filter(user=self, active=True).first()

    def get_instructor_group(self):
        if self.user_type == 'student':
            grp = InstructorGroup.objects.filter(students=self).first()
            return grp.id
        elif self.user_type == 'instructor':
            grp = InstructorGroup.objects.filter(instructor=self).first()
            return grp.id

    def get_id(self):
        instructor_group_id = self.get_instructor_group()
        if instructor_group_id:
            return f"{self.id:03d}{self.school_code}_{instructor_group_id}"
        else:
            return f"{self.id:03d}{self.school_code}"

    @property
    def player(self):
        return Player.objects.filter(
            user=self,
            active=True
        ).first()

    @property
    def full_id(self):
        instructor_group_id = self.get_instructor_group()
        return f"{self.id:03d}{self.school_code}_{instructor_group_id}"

    user_type = models.CharField(
        max_length=10,
        choices=(('student', 'student'), ('oc', 'oc'),('admin', 'admin'), ('instructor', 'instructor'),
                 ('vip', 'vip')),
        blank=True, null=True
        )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True )
    school = models.CharField(max_length=100, blank=True, null=True)
    encrypted_id = models.CharField(max_length=32, default=get_random_string(length=32))
    school_code = models.CharField(max_length=2, blank=True, null=True)
    
class InstructorGroup(models.Model):
    def get_player(self):
        players = Player.objects.filter(user__in=self.students.all()).order_by('-active')
        return players

    instructor = models.ManyToManyField('account.User', related_name='instructor')
    students = models.ManyToManyField('account.User', related_name='student')