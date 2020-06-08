from django.conf.urls import url
from django.urls import path
from . import views 

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'api/', views.inputCommand),
    url(r'updateState/', views.updateState),
    url(r'displayGraph/', views.displayGraph),
]

