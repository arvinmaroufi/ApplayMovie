from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 100:
            raise ValidationError("نام کاربری نمی ‌تواند بیشتر از 100 کاراکتر باشد.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("نام کاربری وارد شده از قبل وجود دارد.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) > 100:
            raise ValidationError("ایمیل نمی ‌تواند بیشتر از 100 کاراکتر باشد.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("ایمیل وارد شده از قبل وجود دارد.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد.")
        if len(password) > 20:
            raise ValidationError("رمز عبور نباید بیشتر از 20 کاراکتر باشد.")
        return password


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("نام کاربری یا رمز عبور نادرست است.", code='invalid_info')
