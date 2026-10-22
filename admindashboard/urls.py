from django.urls import path
from . import views
urlpatterns = [
    path('top_purchaser/', views.top_purchaser, name='admindashboard.top_purchaser'),
    path('top_purchasers/', views.top_purchasers, name='admindashboard.top_purchasers'),
]