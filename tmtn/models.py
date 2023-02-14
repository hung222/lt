from django.db import models
class tn(models.Model):
       tennv = models.CharField(max_length=800)
       theloai = models.CharField(max_length=1200)
       congnang = models.CharField(max_length=1500)
