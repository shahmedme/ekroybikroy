from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/id=<int:id>', views.postDetails, name='post-details'),
    path('posts/', views.category, name='category'),
    path('create/', views.create, name='add-post'),
]
