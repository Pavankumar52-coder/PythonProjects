from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    file = CloudinaryField('Images')
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)