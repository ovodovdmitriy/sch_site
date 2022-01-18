from django.urls import path,include
from . import views

urlpatterns = [
    path(r'babushkinsky',views.babush, name='babu'),
    path(r'sviblovo',views.sviblovo, name='svib'),
    path(r'alekseevsky',views.aleks, name='aleks'),
    path(r'severnoyemedvedkovo',views.smedved, name='smedved'),
    path(r'altufevsky',views.altu, name='altu'),
    path(r'bibirevo',views.bibi, name='bibi'),
    path(r'butyrsky',views.buty, name='buty'),
    path(r'lianozovo',views.lian, name='lian'),
    path(r'losinoostrovsky',views.los, name='los'),
    path(r'marfino',views.marf, name='marf'),
    path(r'marynaroshya',views.mary, name='mary'),
    path(r'ostankinsky',views.ost, name='ost'),
    path(r'otradnoye',views.otr, name='otr'),
    path(r'rostokino',views.ros, name='ros'),
    path(r'severniy',views.sev, name='sev'),
    path(r'yujnoyemedvedkovo',views.ymedved, name='ymedved'),
    path(r'yaroslavskiy',views.yar, name='yar'),
    path('', views.index, name='Main'),
]
