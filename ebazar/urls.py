from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('details/id=<int:id>', main_views.postDetails, name='post-details'),
    path('posts/', main_views.category, name='category'),
    path('login/', main_views.login, name='login-page'),
    path('signup/', main_views.signup, name='signup-page'),
    path('confirm-signup/', main_views.c_signup, name='Confirm-signup-page'),
    path('create/', main_views.create, name='add-post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
