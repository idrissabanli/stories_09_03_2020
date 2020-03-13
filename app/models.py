from django.db import models


class Story(models.Model):
    CATEGORIES = (('d', 'DESSERT'), ('s', 'SUP'),)
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORIES, max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='stories', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create other models
# Recipe
# Author
# Category
# Comment
# Comment reply