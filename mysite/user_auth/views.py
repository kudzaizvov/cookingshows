from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password1(self):
        password1 = self.cleaned_data.get('password')
        validate_password(password1, self.instance)
        return password1


def user_login(request):
  return render(request, 'authentication/login.html')


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    print(username, password)
    if user is None:
        errors = "Invalid login credentials."
        messages.error(request, errors) 
        return HttpResponseRedirect(
        reverse('user_auth:login')   
        )
    else:
        login(request, user)
        print("redirecting")
        return HttpResponseRedirect(
            reverse('cookingshow:index')
        )
    
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_auth:login'))
        else:
            # Check for password validation errors
            password_errors = form.errors.get('password')
            if password_errors:
                for error in password_errors:
                    messages.error(request, f"Password: {error}")
            else:
                # If there are other form errors, display them as before
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})
