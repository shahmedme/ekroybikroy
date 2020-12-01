from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('posts/<slug:product_slug>/', views.post_details, name='post-details'),
    path('add-post/', views.add_post, name='add-post'),
    path('setup-site/', views.setup_site, name='setup-site'),
    path('action-handler/', views.action_handler, name='action-handler'),
]
