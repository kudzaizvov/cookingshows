from django.urls import path, include, re_path
from . import views

app_name = 'cookingshow'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:show_id>', views.detail, name='detail'),
    path('create/', views.create_show, name='create_show')
]