from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create/', views.create, name="create"),
    path('results/<id>', views.results, name="results"),
    path('vote/<id>', views.vote, name="vote"),
    path('delete/<id>', views.delete, name="delete"),
    path('profile/', views.profile, name="profile"),
    path('register/', views.register, name="registration"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
]
