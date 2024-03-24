from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('user_panel/', views.user_panel, name="user_panel"),
    path('data_coll/', views.data_coll, name="data_coll"),
    path('dash/', views.dash, name="dash"),
    path('disruption/', views.disruption, name="disruption")
]
