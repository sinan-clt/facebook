from django.urls import path,include
from . import views


urlpatterns = [
    path('test1',views.test1,name='test1'),

    path('facebook/',views.facebook,name='facebook'),
    path('login/',views.fnlogin,name='login'),
    path('changepass/',views.changepass,name='changepass'),
    path('profile/',views.profile,name='profile'),
]