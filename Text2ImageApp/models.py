from django.db import models

# Create your models here.
from django.db import models


class GeneratedImage(models.Model):
    image = models.FileField(upload_to='generated_images/')
