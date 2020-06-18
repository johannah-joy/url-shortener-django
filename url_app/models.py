from django.db import models
# from django.utils import timezone

# Create your models here.

class Storage(models.Model):
  long_url = models.URLField(null=True)
  short_url = models.URLField(unique=True, max_length=6)
  num_clicks = models.IntegerField(default=0)
  created_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.long_url}, {self.short_url}'

  def clicked(self):
    self.num_clicks += 1
    self.save()