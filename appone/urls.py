from django.urls import path
from .views import register_request,login_request,logout_request
urlpatterns = [
    path('userregister/',register_request ),#http://127.0.0.1:8000/ap1/userregister/
    path('loginuser/',login_request),#http://127.0.0.1:8000/ap1/loginuser/
    path('logoutuser/',logout_request),#http://127.0.0.1:8000/ap1/logoutuser/
]