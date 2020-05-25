from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event_type = ArrayField(models.CharField(max_length=200), blank=True)
    max_radius = models.PositiveIntegerField()

    def __str__(self):
        return "Profil de {0}".format(self.user.username)

class Event(models.Model):
    record_id = models.CharField(max_length=200, null=True)
    profiles = models.ManyToManyField(Profile)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    like_number = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField(default=None, blank=True, null=True)
    end_time = models.DateTimeField(default=None, blank=True, null=True)
    last_update = models.DateTimeField(default=None, blank=True, null=True)
    venue_name = models.CharField(max_length=200, null=True)
    venue_adress = models.CharField(max_length=200, null=True)
    postal_code = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=15, null=True)
    free_of_charge = models.BooleanField(default=True)
    pic_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
