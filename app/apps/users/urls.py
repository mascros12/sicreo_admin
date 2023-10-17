from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('', views.user_list, name='user_list'),
    path('delete/<int:pk>', views.UserDelete.as_view(), name='UserDelete'),
    path('edit/<int:pk>', views.UserUpdate.as_view(), name='UserUpdate'),
    path('password/<int:user_id>/', views.change_password, name='change_password'),
]
