from django.urls import path
from elderhelper import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate_text, name='generate_text'),
    # path('chat', views.chat, name='chat'),
]