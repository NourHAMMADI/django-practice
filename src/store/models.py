from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  summary = models.TextField(null=True, blank=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
  
