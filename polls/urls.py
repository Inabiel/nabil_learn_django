from django.urls import path
from .controller.user import *

urlpatterns = [
    path('user', get_user),
    path('user/create', create_user)
]
