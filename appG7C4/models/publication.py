from django.db import models

from .product_category import ProductCategory
from .user import User

# Creating a Publication model
class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='app/publications/', blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title