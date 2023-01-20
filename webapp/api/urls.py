from django.urls import path
from api.views import *

urlpatterns = [
    path("users/", users),
    path("forests/", all_forest)
]