from django.db import models
from django.urls import reverse

# Create your models here.

TASTES = (
  ('S1', 'Sweet'),
  ('S2', 'Salty'),
  ('S3', 'Savory'),
  ('S4', 'Spicy'),
  ('S5', 'Sour'),
  ('B1', 'Bitter')
)

class Taste(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=100)

  def __str__(self):
    return self.name

class Snack(models.Model):
  name = models.CharField(
    max_length=50,
    unique=True
    )
  description = models.TextField(max_length=250)
  prep_time = models.PositiveIntegerField(
    db_column = 'Prepartion Time',
    help_text = 'Enter the time it takes to prepare the snack/food in minutes.'
    )
  tastes = models.ManyToManyField(Taste)
  
  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('snacks')
  
class Comment(models.Model):
  title = models.CharField(max_length=50)
  comment = models.TextField(max_length=250)
  snack = models.ForeignKey(Snack, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.title}'