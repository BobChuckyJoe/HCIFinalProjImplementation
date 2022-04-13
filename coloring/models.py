from django.db import models

# The Author model has been created for you
class Author(models.Model):
  name = models.CharField(max_length=50)

# Create the Drawing model
class Drawing(models.Model):
  author_name = models.CharField(max_length=50, default="")
  title = models.CharField(max_length=50, default="")
  points = models.TextField(default="[]")