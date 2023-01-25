from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tasks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Teeth(models.Model):
    TOOTH_CHOICES = (
        ('cleaning', 'cleaning'),
        ('lorem', 'lorem'),
        ('ipsom', 'ipsom')
    )

    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tooth1 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth2 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth3 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth4 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth5 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth6 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth7 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth8 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth9 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth10 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth11 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth12 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth13 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth14 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth15 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth16 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth17 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth18 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth19 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth20 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth21 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth22 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth23 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth24 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth25 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth26 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth27 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth28 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth29 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth30 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth31 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
    tooth32 = models.CharField(max_length=32, choices=TOOTH_CHOICES, default='lorem')
