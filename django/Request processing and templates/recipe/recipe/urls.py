from calculator import views
from django.urls import path

urlpatterns = [
    path('omlet/', views.handler_omlet),
    path('pasta/', views.handler_pasta),
    path('buter/', views.handler_buter)
]