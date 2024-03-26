from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<str:room>/',views.RomeView.as_view(), name='room'),
    path('send',views.send_message, name='send'),
    path('get/<str:room>',views.get_messages,name='get'),
    
    
]
