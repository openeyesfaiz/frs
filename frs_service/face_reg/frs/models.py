from django.db import models
from django.utils import timezone

# Create your models here.
class Mon(models.Model):
    
    def videoname():
        return timezone.localtime(timezone.now()).strftime('%Y%m%d%H%M%S')
    
    name = models.CharField(max_length=14, default=videoname())

class Image(models.Model):
    mon = models.ForeignKey('Mon', on_delete=models.CASCADE)
    src = models.ImageField(upload_to='video/')