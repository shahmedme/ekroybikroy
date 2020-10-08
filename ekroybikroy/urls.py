from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from search import views as search_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('account.urls')),
    path('search/', search_views.product_search, name="product_search")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
