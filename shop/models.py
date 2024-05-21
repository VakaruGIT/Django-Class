from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=20)
    class Meta:
        db_table = 'product'
    def __str__(self):
        return self.name

