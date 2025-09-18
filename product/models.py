from django.db import models


class Audience(models.Model):
    name = models.CharField(max_length=50)  # Men, Women, Kids

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)  
    audience = models.ForeignKey(Audience, on_delete=models.CASCADE, related_name="categories")

    class Meta:
        unique_together = ('name', 'audience')  

    def __str__(self):
        return f"{self.name} ({self.audience.name})"
    
    
class Product(models.Model):
    SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=2, choices=SIZES)
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_available(self):
        return self.stock > 0

    def __str__(self):
        return f"{self.name} - {self.category.name} - {self.category.audience.name}"
