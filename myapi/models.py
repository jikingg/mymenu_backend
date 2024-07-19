from django.db import models

# Create your models here.
class MealPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    time = models.BigIntegerField()
    recipeURL = models.TextField()
    imageURL = models.TextField()

    def __str__(self):
        return self.title