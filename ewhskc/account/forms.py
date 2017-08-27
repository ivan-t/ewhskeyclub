from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.validators import RegexValidator

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Incorrect username or password.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect username or password.")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
    letters_only = RegexValidator(r'^[a-zA-Z]+$', 'This field must contain only letters.')
    alphanumeric = RegexValidator(r'^[a-zA-Z0-9]+$', 'This field must contain only letters or numbers.')

    username = forms.Field(label='Username', validators=[alphanumeric])
    email = forms.EmailField(label='Email')
    confirm_email = forms.EmailField(label='Confirm email')
    first_name = forms.Field(label='First name', validators=[letters_only])
    last_name = forms.Field(label='Last name', validators=[letters_only])
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'confirm_email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
        ]

    def clean_confirm_email(self):
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('confirm_email')
        if email != confirm_email:
            raise forms.ValidationError("Emails must match.")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("A user has already registered with that email.")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords must match.")
        return password