from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('create_post/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_page, name='post'),
]