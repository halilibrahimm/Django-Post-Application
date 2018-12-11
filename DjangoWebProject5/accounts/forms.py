from django import forms
from django.contrib.auth import authenticate,login
from django.contrib.auth.models  import User



class LoginForm(forms.Form):#giriş yapmak için
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get('username')# cleaned metodu doğruysa içerikleri eşitliğin karşısına atar
        password=self.cleaned_data.get('password')
        if username and password:
            user=authenticate(username=username,password=password)#sistemde bilgiler burada kontrol ediliyor
            if not user:
                raise forms.ValidationError('Kullanıcı Adını ve parolayı yanlış girdiniz')
        return super(LoginForm,self).clean()




class RegisterForm(forms.ModelForm): #siteye üye olmak için
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput) 


    class Meta:
        model=User
        fields=[
            'username',
            'password1',
            'password2',
            ]


    def clean_password2(self):#şifrelerin aynı olup olmadığını kontrol etmek için fonksiyon yazdık
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError('parolalar eşleşmiyor')
        return password2
