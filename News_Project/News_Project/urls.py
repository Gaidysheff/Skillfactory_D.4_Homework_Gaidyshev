
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('newsapp.urls')),
    path('news/search/', include('newsapp.urls')),
    path('articles/', include('newsapp.urls_for_articles')),
]
