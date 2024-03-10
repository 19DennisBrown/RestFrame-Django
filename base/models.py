from django.db import models

# Create your models here.

class Person(models.Model):
  name = models.TextField(max_length = 20)
  country = models.TextField(max_length = 20)
  language = models.TextField(max_length = 20)
  province = models.TextField(max_length = 20)
  data_date = models.DateTimeField(auto_now_add = True)
  
  def __str__(self):
    return self.name