from django.db import models

# Create your models here.

class ContactPerson(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    contact_number = models.IntegerField()