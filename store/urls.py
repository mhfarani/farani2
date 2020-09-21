from django.urls import path
from store import views
from .models import product

urlpatterns = [
    path('', views.home, name='store_home'),
    path('about/', views.about, name='about'),
    path('buy/<int:pr>', views.addbuy, name='add'),

]
