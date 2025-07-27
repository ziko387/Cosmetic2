from django.db import models


# Create your models here.
class cosmeticItems(models.Model):
    item = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='cosmetic_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=[
        ('skincare', 'Skincare'),
        ('makeup', 'Makeup'),
        ('haircare', 'Haircare'),
        ('fragrance', 'Fragrance'),
        ('tools', 'Tools'),
        ('nails', 'Nails'),
    ])
    Area = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
        
class Order(models.Model):
    item= models.ForeignKey(cosmeticItems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)   
    userEmail = models.EmailField()
    shipping_address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)     
    def __str__(self):
        return f"Order {self.id}-{self.item.item}-{self.quantity}pcs-{self.order_date.strftime('%Y-%m-%d %H:%M:%S')}"
    
class user(models.Model):
    username= models.CharField(max_length=170, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)


class userProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile -{self.profile_picture.url if self.profile_picture else 'No Picture'}"
     
    


  

