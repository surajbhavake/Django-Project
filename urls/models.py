from django.db import models

# Create your models here.
class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)