from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='AiHome'),
    path('about/', views.about, name='About-we'),

]