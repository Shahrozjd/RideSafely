from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('challans/',views.challans, name='challans'),
        path('showchallandata/',views.showchallandata, name='showchallandata')
]