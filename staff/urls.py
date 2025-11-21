from django.urls import path
from staff import views

app_name = "staff"

urlpatterns =[
    path('', views.dashboard, name='dashboard_page'),
    path('signin/', views.sign_in, name='signin_page'),
    path('signup/', views.sign_up, name='signup_page'),
    path('userdash/', views.user_dashboard, name='user_page'),
    path('prodash/', views.product_dashboard, name='product_page'),
    path('edit-booking/<str:bookin_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<str:bookin_id>/', views.delete_booking, name='delete_booking'),
    path('logout_user/', views.logout_user, name='logout_user'),
]

