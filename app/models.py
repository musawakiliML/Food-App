from django.db import models

# Create your models here.
class Item(models.Model):
   item_name = models.CharField(max_length=200)
   item_desc = models.CharField(max_length=200)
   item_price = models.IntegerField()
   item_image = models.CharField(max_length=600, default="https://static.vecteezy.com/system/resources/previews/003/170/825/original/isolated-food-plate-fork-and-spoon-design-free-vector.jpg")

   def __str__(self):
       return self.item_name