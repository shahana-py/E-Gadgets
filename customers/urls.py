from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import login_view

urlpatterns = [
    path('account', views.show_account,name='accountpg'),
    path('logout', views.sign_out,name='logout'),
    path('login/', login_view, name='login'),
    
    
]
