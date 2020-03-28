from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class stock(models.Model):
    item = models.CharField(max_length=200)
    qnt = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(100)])


