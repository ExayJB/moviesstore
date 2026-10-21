from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.models import User
from cart.models import Item


def top_purchaser(request):
    ranking = (User.objects.annotate(movies_purchased=Sum('order__item__quantity')).filter(movies_purchased__gt=0).order_by('-movies_purchased'))
    top_user = ranking.first()
    top_user_movies = []
    if top_user:
        top_user_movies = (Item.objects.filter(order__user=top_user).values('movie__id', 'movie__name').annotate(total_qty=Sum('quantity')))
    template_data = {}
    template_data['title'] = 'Admin Dashboard - Top Purchaser'
    template_data['top_user'] = top_user
    template_data['top_user_movies'] = top_user_movies
    template_data['ranking'] = ranking
    return render(request, 'admindashboard/top_purchaser.html', {'template_data': template_data})
