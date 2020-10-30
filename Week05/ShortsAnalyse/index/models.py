from django.db import models

# Create your models here.
class Shorts(models.Model):
    # id=models.AutoField(primary_key=True)
    star=models.IntegerField()
    rate = models.CharField(max_length=10)
    short = models.CharField(max_length=255)

    class Meta:
        # managed=False
        db_table = 'shorts'
