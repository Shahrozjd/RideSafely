from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('challans/',views.challans, name='challans'),
    path('showchallandata/',views.showchallandata, name='showchallandata'),
    path('graphs/', views.graphs, name='graphs'),
    path('graph1/', views.graph1, name='graph1'),
    path('graph2/', views.graph2, name='graph2'),
]