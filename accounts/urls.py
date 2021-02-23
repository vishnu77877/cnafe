from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('jp', views.jp, name='jp'),
    path('jps', views.jps, name='jps'),
    path('aj', views.aj, name='aj'),
    path('ajs', views.ajs, name='ajs'),
    path('logout', views.logout, name='logout'),
    path('cna/', include('cna.urls'))


]
