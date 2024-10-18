from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    online_rating = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ccscore = models.IntegerField()
    amazonreviews = models.JSONField(default=list)
    flipkartreviews = models.JSONField(default=list)

    def __str__(self):
        return self.title