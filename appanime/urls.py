"""appanime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from anime import views as animeView
from anime.views import search_anime, search_results, AnimeDetailView, home, anime_list, on_going
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('search/', search_anime, name='search_anime'),
    path('on_going/', on_going, name='on_going'),
    path('results/<str:query>/', search_results, name='search_results'),
    path('anime/<int:pk>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('anime/', anime_list, name='anime_list'),
]

# sampe bikin urls buat on-going anime, views, urls, ama base html

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)