from django.forms import ModelForm
from .models import Orders,Product,Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Orderform(ModelForm):
    class Meta:
        model=Orders
        fields='__all__'

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
