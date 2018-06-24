from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(u'姓名', max_length=10)
    password = models.CharField(u'密码', max_length=20, blank=True)

    def __str__(self):
        return self.name
