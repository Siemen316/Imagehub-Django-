from django.db import models

# Create your models here.

class image(models.Model):
    img_name = models.CharField(max_length = 250)
    img_desc = models.TextField()
    img_by = models.CharField(max_length = 250,default="siemen")
    img_url = models.CharField(max_length = 250)

    def __str__(self):
        return self.img_name

