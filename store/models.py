from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Jewels(models.Model):
    jewel_name = models.CharField(max_length=50, unique=True, null=False)
    jewel_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    jewel_size = models.TextField(null=True)
    jewel_weight = models.TextField(null=True)
    jewel_origin = models.TextField(null=True)
    jewel_image = models.ImageField(upload_to='store/jewellery_images/', null=False)
    jewel_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jewels', null=False)


    def __str__(self):
        return self.jewel_name
    

# class Orders(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     jewels = models.ForeignKey(Jewels, on_delete=models.CASCADE)
#     ordered_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f"Order by {self.user.username} - {self.jewels.jewel_name}"
    




