from django.db import models
from django.core.urlresolvers import reverse


class Owner(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})


class Animal(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey('Owner', blank=True, null=True)

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
