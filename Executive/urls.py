from django.urls import path, include
from .views import *

urlpatterns = [
    path('pending_car_approval/', pending_car_approval, name='pending_car_approval'),

]
