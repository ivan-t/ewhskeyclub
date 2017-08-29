from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.validators import RegexValidator

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def __init__(self):
        super(LoginForm, self).__init__()
        for field in self.fields:
            self.fields[field].required = True

    def clean(self):
        username = self.cleaned_data.get("username").lower()
        password = self.cleaned_data.get("password").lower()

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
    letters_only = RegexValidator(r'^[a-zA-Z\-]+$', 'This field cannot have spaces and must contain only letters or hypens.')
    alphanumeric = RegexValidator(r'^[a-zA-Z0-9]+$', 'This field must contain only letters or numbers.')

    username = forms.Field(label='Username', validators=[alphanumeric], widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    confirm_email = forms.EmailField(label='Confirm email', widget=forms.EmailInput(attrs={'placeholder':'Confirm email'}))
    first_name = forms.Field(label='First name', validators=[letters_only], widget=forms.TextInput(attrs={'placeholder':'First name'}))
    last_name = forms.Field(label='Last name', validators=[letters_only], widget=forms.TextInput(attrs={'placeholder':'Last name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}), label='Confirm password')

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

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name').lower()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name').lower()
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        return email

    def clean_confirm_email(self):
        email = self.cleaned_data.get('email').lower()
        confirm_email = self.cleaned_data.get('confirm_email').lower()
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