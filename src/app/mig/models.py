from django.db import models


# Create your models here.
class init_user(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=60)

    class Meta:
        db_table = 'db_user'
