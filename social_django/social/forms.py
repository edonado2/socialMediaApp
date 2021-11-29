from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    pasword1 = forms.CharField(label ='Enter Pasword', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k:"" for k in fields}
        
class PostForm(forms.ModelForm):
    content = forms.CharField(label ='',widget=forms.Textarea(attrs={'placeholder':'What\'s on your mind?','rows':5,'cols':50}), required=True)
    
    class Meta:
        model = Post
        fields = ['content']