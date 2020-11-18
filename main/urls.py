from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/id=<int:id>', views.post_details, name='post-details'),
    path('posts/', views.posts, name='posts'),
    path('add-post/', views.add_post, name='add-post'),
    path('setup-site/', views.setup_site, name='setup-site'),
    path('action-handler/', views.action_handler, name='action-handler'),
]
