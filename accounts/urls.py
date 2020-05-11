from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^begin_password_reset/?$', views.password_reset, name='pasword_reset'),
]
