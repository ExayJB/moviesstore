"""
URL configuration for moviesstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.shortcuts import render

def admin_comment_statistics(request):
    User = get_user_model()
    users = (User.objects.annotate(comment_count=Count('review')).filter(comment_count__gt=0).order_by('-comment_count', 'username'))
    context = {**admin.site.each_context(request), 'title': 'Comment Statistics', 'top_user': users.first(), 'users': users,}
    return render(request, 'admin/comment_statistics.html', context)

urlpatterns = [
    path('admin/comment-statistics/', admin.site.admin_view(admin_comment_statistics), name='admin_comment_statistics'),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('movies/', include('movies.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)