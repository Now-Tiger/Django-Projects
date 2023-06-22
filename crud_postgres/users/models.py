from django.db import models

# USER -> id(AutoField), name(CharField), gender(CharField), age(IntegerField)
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()