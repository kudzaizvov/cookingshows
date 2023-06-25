from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Show
from django import forms

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['show_name', 'description', 'show_date']
        widgets = {
            'show_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'show_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

def index(request):
    all_shows = Show.objects.all()
    context = {'all_shows': all_shows}
    return render(request, "shows.html", context)

def detail(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    return render(request, 'details.html', {'show': show})

@login_required(login_url="/accounts/login")
def create_show(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect(
                reverse('cookingshow:index')
            )  # Redirect to a login page
    else:
        form = ShowForm()
    return render(request, 'show_create.html', {'form': form})