from django.db import models

# Create your models here.


class Superhero(models.Model):
    name = models.CharField(max_length=30)
    alter_ego = models.CharField(max_length=30)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=100)
    date_introduced = models.DateField()

    def __str__(self):
        return self.name


