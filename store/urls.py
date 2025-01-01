from django.urls import path

from django.contrib.auth import views as auth_views

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

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="store/registrations/reset_password_form.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="store/registrations/reset_password_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="store/registrations/reset_password_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="store/registrations/reset_password_complete.html"), name="password_reset_complete"),
]