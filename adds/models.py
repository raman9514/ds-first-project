from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=40 , primary_key=True)
    
    def __str__(self):
        return self.category


class Position(models.Model):
    position=models.CharField(max_length=50 , primary_key=True)
    
    def __str__(self):
        return self.position

class Adds(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=50)
    banner = models.ImageField(upload_to="Adds/banner")
    positions = models.ForeignKey(Position,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    payment = models.IntegerField()

    
    def __str__(self):
        return self.name
