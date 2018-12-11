from django import forms
from .models import Post
from .models import Comment
from captcha.fields import ReCaptchaField#captcha için

class PostForm(forms.ModelForm):
   # captcha = ReCaptchaField() #captcha alanı oluşturur formda
    class Meta:
        model=Post
        fields=[
            'title',
            'content',
            'image',
            ]

class CommentForm(forms.ModelForm):
   # captcha = ReCaptchaField()#captcha alanı oluşturur formda
    class Meta:
        model=Comment
        fields=[
            'name',
            'content',
            ]