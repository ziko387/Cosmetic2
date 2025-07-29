from django import forms
from .models import cosmeticItems, Order, user

class CosmeticItemForm(forms.ModelForm):
    class Meta:
        model = cosmeticItems
        fields = ['item', 'price', 'description', 'image', 'category', 'Area']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'quantity', 'total_price', 'userEmail', 'shipping_address'] 

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username', 'email', 'password', 'phonenumber']
        widgets = {
            'password': forms.PasswordInput(),
        }               

