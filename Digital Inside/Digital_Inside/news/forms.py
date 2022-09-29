from .models import Post, Comments
from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =['title', 'image',  'contents']

        widgets ={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название записи'
            }),
            "contents": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст статьи'
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields =['content']

        widgets ={
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст комментария'
            })
        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Потдвердите пароль'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почта'}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
