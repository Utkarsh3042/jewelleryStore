from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:pk>/', views.details, name='details'),
    path('category/<int:pk>', views.category, name='category'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('search/', views.search_view, name='search_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('adminpanel/add/', views.add_jewellery, name='add_jewellery'),
    path('adminpanel/edit/<int:pk>', views.edit_jewellery, name='edit_jewellery'),
    path('adminpanel/delete/<int:pk>', views.delete_jewellery, name='delete_jewellery'),
    path('about/', views.about, name='about'),
]