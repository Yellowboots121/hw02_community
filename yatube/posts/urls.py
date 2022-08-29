from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'main_page'), #Главная страница
    path('group/<slug>/', views.group_posts, name = 'group_list'), #Страница с постами
]