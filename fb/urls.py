from django.urls import path,include
from . import views


urlpatterns = [
    path('facebook',views.facebook,name='facebook')
]