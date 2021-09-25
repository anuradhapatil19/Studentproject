from django.contrib.auth.decorators import login_required
from  django.urls import path
from .views import create_product,list_product,detail_product

urlpatterns=[
    path('createpd/',login_required(create_product.as_view()),name='pd'),#http://127.0.0.1:8000/ap2/createpd/
    path('pdlist/',login_required(list_product.as_view()),name='list'),#http://127.0.0.1:8000/ap2/pdlist/
    path('<pk>/pddetail/',login_required(detail_product.as_view()),name='detail'),#http://127.0.0.1:8000/ap2/1/pddetail/
]