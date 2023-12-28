from django import forms
from .models import Products,Category,User,Checkout
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['category','name','seller','product_image','quantity','orginal_price','selling_price','description','bestseller','status']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product_image'].widget.attrs['accept'] = 'image/*'


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name','address','phone_number']

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control me-2',
            'type': 'search',
            'placeholder': 'Search...',
            'aria-label': 'Search',
            'style': 'position: relative; left: -3vh; display: flex; height: 48px; align-items: center; z-index: 1; width: 100vh;'
        })
    )
