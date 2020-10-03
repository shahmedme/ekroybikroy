from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login-page'),
    path('signup/', views.signup, name='signup-page'),
    path('logout/', views.logout, name='logout')

]
