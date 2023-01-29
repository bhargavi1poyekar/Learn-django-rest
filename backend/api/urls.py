from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns=[
    path('auth/',obtain_auth_token),
    path('',views.api_home), # Can also import from .view import api_home and then direct use api_home
    # http://localhost:8000/api
    path('model',views.api_model),
    path('rest',views.api_rest),
    path('rest_post',views.api_post),

]