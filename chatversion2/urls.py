# chat/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('userlogin/',views.login_view,name="userlogin"),
    path('userlogout/',views.logout_view,name="userlogout"),
    path("<str:room_name>/", views.room, name="room"),

]